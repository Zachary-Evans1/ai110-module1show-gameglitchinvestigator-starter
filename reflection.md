# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
  
  The game was a number guessing game with 3 difficulites. It had a developer debug info box, an area to enter a guess, a submit guess button, a new game button and a show hint check mark box.

- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").

  The hints were backwards, it said go lower when the number was higher and vice versa.
  The "You already won. Start a new game to play again." text does not go away after a new game, and the guess box does not allow any new guesses after a game is won.
  The amount of attempts it said I had in the blue textbox changed when I changed the dificulty, even without starting a new game.
  The code allows inputs outside the range, I was able to enter -10 and 1000
  The dificultly setting dont seem to change anything besides the amount of attempts, when I select easy or hard it still tells me I have to guess a number between 1 and 100. and the debug secrets still go above 20 and 50
  Sometimes it doesn't accept an input and the history shows it submitted the old guess.
  The code does not allow inputs after a winning guess is entered.



**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input |           Expected Behavior | Actual Behavior | Console Output / Error |
|-------|         -------------------|-----------------|------------------------|
|Difficulty: Easy|  1 <= secret <=20    Secret = 78      None
| 99   |           Go Lower            Nothing           None
| 1000  | Error               Go Higher         None

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?

Claude code,

- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).


- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
