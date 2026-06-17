# AI Interactions Log

> **Stretch features only.** Only fill in the sections that apply to stretch features you attempted. If you did not attempt a stretch feature, leave its section blank or delete it. This file is not required for the core project.

---

## Agent Workflow (SF8)

> Document your experience using an AI agent (e.g., Cursor Agent, Claude, Copilot) to make multi-step changes autonomously.

**What task did you give the agent?**

<!-- Describe the goal you asked the agent to accomplish -->

**What did the agent do?**

<!-- List the steps the agent took (files edited, commands run, etc.) -->

**What did you have to verify or fix manually?**

<!-- Describe anything the agent got wrong or that required human review -->

---

## Test Generation (SF7)

> Document how you used AI to help generate or improve tests.

I used a single AI prompt asking for all five edge case tests, here it is: Can you make me some pytest tests that hit 5 edge case inputs, I'm thinking a sentence/string input, a negative number,  a very large number, maybe a floating point number, and finally and empty input like " " or ""? @app.py  @logic_utils.py  @tests/test_game_logic.py

1:
    Case: String input
    Prompt: Above
    AI-Suggested Test: test_parse_guess_sentence_input: verifies "hello world" is rejected
    Did It Pass?: Yes
    My Reasoning: The game should be able to deal with a string input without crashing and report a clear and correct error message to the user.
2:
    Case: Negative Number
    Prompt: Above
    AI-Suggested Test: test_parse_guess_negative_number: verifies "-42" is parsed correctly
    Did It Pass?: Yes
    My Resoning: Negative numbers are still valid intgers in Python, so the game should not have any trouble parsing a negative number guess like -42.
3:
    Case: Very Large Number
    Prompt: Above
    AI-Suggested Test: test_parse_guess_very_large_number: verifies "999999999999" is accepted
    Did It Pass?: Yes
    My Reasoning: Python does not have a limit for integers like Java or C, so a very large number like 999999999999 should be parsed correctly.
4:
    Case: Floating Point Number
    Prompt: Above
    AI-Suggested Test: test_parse_guess_floating_point_number: verifies "42.7" is converted to 42
    Did It Pass?: Yes
    My Reasoning: The code converts floating point numbers using "int(float(raw))" So a floating point number should be converted to an integer. 42.7 should convert to 42 and be parsed correctly.
5:
    Case: Empty Input
    Prompt: Above
    AI-Suggested Test: test_parse_guess_empty_string: verifies "" is rejected
    Did It Pass?: Yes
    My Resoning: An empty input should be rejected safely without the game crashing and the user should recive an error message. Testing "" makes sure even if the guess box is empty, the game will deal with the input gracefully.

---

## Linting & Style (SF9)

> Document your use of AI for linting or code style improvements.

**Prompt used:**

```
<!-- Paste the prompt you gave the AI -->
```

**Linting output before:**

```
<!-- Paste relevant linter warnings/errors -->
```

**Changes applied:**

<!-- Describe what you changed based on the AI's suggestions -->

---

## Model Comparison (SF11)

> Compare two AI models on the same task.

**Task given to both models:**

<!-- Describe what you asked each model to do -->

| | Model A | Model B |
|-|---------|---------|
| **Model name** | | |
| **Response summary** | | |
| **More Pythonic?** | | |
| **Clearer explanation?** | | |

**Which did you prefer and why?**

<!-- Your conclusion -->
