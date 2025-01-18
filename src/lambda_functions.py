import os
import json
import urllib.request
import boto3
from datetime import datetime, timedelta, timezone

def format_game_data(game):
    status = game.get("status", "Unknown")
    away_team = game.get("awayTeam", {}).get("name", "Unknown")
    home_team = game.get("homeTeam", {}).get("name", "Unknown")
    final_score = f"{game.get('score', {}).get('fullTime', {}).get('awayTeam', 'N/A')}-{game.get('score', {}).get('fullTime', {}).get('homeTeam', 'N/A')}"
    start_time = game.get("utcDate", "Unknown")
    
    # Format scores
    if status == "FINISHED":
        return (
            f"Game Status: {status}\n"
            f"{away_team} vs {home_team}\n"
            f"Final Score: {final_score}\n"
            f"Start Time: {start_time}\n"
        )
    elif status == "LIVE":
        return (
            f"Game Status: {status}\n"
            f"{away_team} vs {home_team}\n"
            f"Current Score: {final_score}\n"
            f"Start Time: {start_time}\n"
        )
    elif status == "SCHEDULED":
        return (
            f"Game Status: {status}\n"
            f"{away_team} vs {home_team}\n"
            f"Start Time: {start_time}\n"
        )
    else:
        return (
            f"Game Status: {status}\n"
            f"{away_team} vs {home_team}\n"
            f"Details are unavailable at the moment.\n"
        )

def lambda_handler(event, context):
    # Get environment variables
    api_key = os.getenv("FOOTBALL_API_KEY")
    sns_topic_arn = os.getenv("SNS_TOPIC_ARN")
    sns_client = boto3.client("sns")
    
    # Adjust for Central Time (UTC-6)
    utc_now = datetime.now(timezone.utc)
    central_time = utc_now - timedelta(hours=6)  # Central Time is UTC-6
    today_date = central_time.strftime("%Y-%m-%d")
    
    print(f"Fetching games for date: {today_date}")
    
    # Fetch data from the Football API (Football-Data.org or similar)
    api_url = f"https://api.football-data.org/v4/matches?date={today_date}"
    
    headers = {
        "X-Auth-Token": api_key
    }
    
    try:
        request = urllib.request.Request(api_url, headers=headers)
        with urllib.request.urlopen(request) as response:
            data = json.loads(response.read().decode())
            print(json.dumps(data, indent=4))  # Debugging: log the raw data
    except Exception as e:
        print(f"Error fetching data from API: {e}")
        return {"statusCode": 500, "body": "Error fetching data"}
    
    # Include all games (final, in-progress, and scheduled)
    messages = [format_game_data(game) for game in data.get('matches', [])]
    final_message = "\n---\n".join(messages) if messages else "No games available for today."
    
    # Publish to SNS
    try:
        sns_client.publish(
            TopicArn=sns_topic_arn,
            Message=final_message,
            Subject="Football Match Updates"
        )
        print("Message published to SNS successfully.")
    except Exception as e:
        print(f"Error publishing to SNS: {e}")
        return {"statusCode": 500, "body": "Error publishing to SNS"}
    
    return {"statusCode": 200, "body": "Data processed and sent to SNS"}
