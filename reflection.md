# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
  
  The game was a number guessing game with 3 difficulties. It had a developer debug info box, an area to enter a guess, a submit guess button, a new game button and a show hint check mark box.

- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").

  The hints were backwards, it said go lower when the number was higher and vice versa.
  The "You already won. Start a new game to play again." text does not go away after a new game, and the guess box does not allow any new guesses after a game is won.
  The amount of attempts it said I had in the blue textbox changed when I changed the difficulty, even without starting a new game.
  The difficulty setting doesn't seem to change anything besides the amount of attempts, when I select easy or hard it still tells me I have to guess a number between 1 and 100. and the debug secrets still go above 20 and 50
  Sometimes it doesn't accept an input and the history shows it submitted the old guess.
  The score will go up even after a wrong guess.
  The code does not allow inputs after a winning guess is entered.



**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input |Expected Behavior | Actual Behavior | Console Output / Error |
|-------|-------------------|-----------------|------------------------|
|Easy   |  1 <= secret <=20    Secret = 78      None
| 99    |  Go Lower            Nothing           None
| 50     |  Score = -5          Score = 5         None

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?

I used Claude Code and ChatGPT.

- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).

One bug I fixed was the score going up on even attempts if the guess was too high, I gave Claude Code this prompt: @app.py  @logic_utils.py  The update_score function seems to have a bug when the score is too high, on even attempts it will award 5 points instead of taking them away, I marked what I believe is the problem on line 41 with a #FIXME comment. can you suggest a fix?

It gave this response: Looking at the update_score function, I see the issue in the "Too High" case:

if outcome == "Too High":
    if attempt_number % 2 == 0:
        return current_score + 5      # Awards points on even attempts!
    return current_score - 5
The problem is that on even attempts, when the guess is too high, it's adding 5 points instead of deducting them. This is inconsistent with the "Too Low" case, which always deducts 5 points regardless of attempt number.

Suggested fix: Remove the conditional and always deduct points, matching the behavior of "Too Low":

if outcome == "Too High":
    return current_score - 5
This makes sense logically — whether the guess is too high or too low, both are wrong guesses and should be penalized the same way. The alternating bonus/penalty based on attempt parity doesn't align with the intended scoring logic.

Would you like me to implement this fix?

I said yes to implementing the fix and had Claude move the function to logic_utils.py. I verified the check worked by having Claude create a pytest function that the code passed, I also verified it by playing the game and seeing that my score went down 5 for too high attempt.

- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

I had another bug in the code where every other guess was being dropped, which was separate from every other guess being turned into a string. I asked Claude Code to help me fix this and it first suggested this fix:

Ah! That's a different issue. The problem is likely that the text input and buttons aren't wrapped in a Streamlit form. Without a form, button state can become unreliable, causing every other submission to be missed.

But I didn't think this would work, instead I asked ChatGPT to write a test line under the if submit: on line 113 that would show up in streamlit, here is the line: 

st.write("Processing:", repr(raw_guess))

When I ran the code after adding this line it would only show the text after every other button press, this told me the problem was that the code was not entering the submit if statement on every other attempt. I then told claude code this: @app.py  Ok I did some tests, the selected line only shows every other time I click the submit button, it's like only every other submit button click goes through.

It then responded with this: Aha! That's the smoking gun—the submit button is only being detected every other click. This is a classic Streamlit issue where the app needs to explicitly rerun after processing a guess.

Add st.rerun() at the end of the submit block to force a fresh rerun and clear the button state

I then let Claude add the single line of code and tested the game. The fix only partially worked: the guesses weren't being dropped anymore, but the hint and winning messages stopped showing. Since I already fixed three other bugs, I decided to leave the problem unresolved instead of continuing to modify the game code and risk introducing more issues.
---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?

I decided a bug was fixed only after I tested the game and made sure the bug wasn't happening during gameplay anymore. I did not rely soley on the AI's suggestions because one of the suggestions was misleading. After fixing a bug, I would boot up the game and repeat the action that led me to finding the bug in the first place.

- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.

One test I ran with pytest was making sure the points went down after each "too high" guess after fixing the related bug. The test sets the score to 100 and the attempt number to 2, it then submits a too high guess and asserts that the score afterwards is 95, or five points lower than the starting score. This test showed me that the fix to the update_score function worked correctly.

- Did AI help you design or understand any tests? How?

Yes, Claude code helped generate a pytest test for the update_score function after I approved its changes to the scoring logic. The generated test allowed me to verify that on an even attempt, a too high guess would correctly take away 5 points from the score, which it was not doing before. In addition to the pytest, I also played the game to confirm the fix worked.

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

A streamlit rerun means that the entire code script is run from top to bottom every time the user interacts with the app, such as clicking a button. Instead of only updating a single part of a page after a user interaction, streamlit refreshes everything and builds the app UI from scratch everytime. This causes varibles not to stick around between interaction unless stored.

Session state is how you store those varibles. It saves the values of the varibles even through the constant reruns of the script. For example, un this project the score, guess, secret and attempts are all stored in the session state. If this project didn't use session state the game would completely reset after each user interaction.

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.

  I think I need to be more clear with my prompts, I had to explain extra things a few times with the bot to make things work correctly. Also, I need to commit more, I made around 4 commits for this project, when I should have made one after every fix.

- What is one thing you would do differently next time you work with AI on a coding task?

Be clearer with prompts and better understand what code the AI is suggesting, I accepted a line of code this project not completely knowing what it did, it fixed the bug I wanted to fix, but it broke the hints system, so I deleted it. If I knew exactly how st.rerun() worked before hand, I could've better critiqued the AI's suggested code.

- In one or two sentences, describe how this project changed the way you think about AI generated code.

This project showed me the power of using AI coding agents, they can speed up programming a lot by making boring code writing fast. At the same time, I learned that using AI to generate code can be frustrating, as it will not always give you exactly what you envisioned. I think I've become both more accepting of AI code, but also more cautious of it.
