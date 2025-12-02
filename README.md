## Inspiration & overview
Upon hearing the theme of _"Odyssey"_, we immediately got inspired with ideas surrounding the Greek myth of the same name. Our idea was to develop a web app that directs the user through a sea of tasks and milestones, be it short-term or long-term, navigating past problems and avoidable tasks. We wanted our app to help the user on their own personal "odyssey", assisting their lifestyle and wellness.
AI implementation was emphasised during this event, so we thought it perfect to implement an AI chatbot, Athena, to assist the user, Odysseus, on their quest for personal growth.

## What it does
An AI chatbot is used to collaborate with the user, similar to Athena's divine assistance in the odyssey. Upon telling the AI your goals and plans, the user will be guided through a series of tasks to reach the end goal.
We planned to implement an online daily journal to encourage daily reflection, and allowing the user to review previous days' entries, though we did not get the chance to develop this.

## How we built it
We built it using a mix of Python (including some python libraries like SQLAlchemy) for the back-end, and HTML, CSS, and ReactJS for the front-end. We utilised Google Gemini's API to implement the AI chatbot, giving it its own ruleset and custom prompts to fine-tune its responses.

## Challenges we ran into
Our biggest challenge came with attempting to force progress with an approach that was really not optimal. Our approaches should have been planned and considered more thoroughly beforehand through effective research.
An example of this is having to rewrite the front-end code to more appropriately implent ReactJS after starting the project with no prior understanding of React and minimal foundational research. We faced similar problems on the backend side using Python and SQLAlchemy, too.


## to run:
`cd` to backend folder
then run `fastapi dev main.py`

then `cd` to "frontend-react"
then run `npm install`
and `npm start`

^ this may not work as some of the python libraries may be missing
