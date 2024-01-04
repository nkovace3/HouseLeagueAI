import csv
from openai import OpenAI
import textwrap

client = OpenAI(api_key="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")

csv_file_path = 'gamestats.csv'
with open(csv_file_path, 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        chatGPTPrompt = "Write in-depth news articles about the following game from the perspective of the first team mentioned:"
        chatGPTPrompt += (
            f'\n\n{row["Team Name"]}, coached by {row["Coach Name"]} '
            f'{row["Won or Lost"]} against {row["Opponent Name"]} {row["Team Score"]} to '
            f'{row["Opponent Score"]} in a {row["Sport"]} game at {row["Venue"]} on {row["Date"]}. '
            f'{row["Performer1"]} ({row["Position1"]}), {row["Performer2"]} ({row["Position2"]}), and {row["Performer3"]} ({row["Position3"]}) '
            f'were top performers. Here is a quick storyline summary of the game: '
            f'{row["Storyline"]}'
        )
        chatGPTPrompt += "\n\nDo not fabricate or specific events in the game done by a certain player; we do not have that information and don't want to make anything up. Do not assume any players' positions; we do not have that information either. Do not mention who scored the goals/runs/baskets/touchdowns (depending on what sport it is).\n"
        completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
        {"role": "system", "content": "You are a local sports writer, skilled in writing exciting, positive stories for the local youth and parents to read about their team."},
        {"role": "user", "content": chatGPTPrompt}
            ]
        )
        print(chatGPTPrompt)
        wrapped_text = textwrap.fill(completion.choices[0].message.content, width=120)
        print(wrapped_text)
