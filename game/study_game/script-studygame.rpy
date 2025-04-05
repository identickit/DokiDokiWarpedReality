init python:
    import random

    def load_questions_from_file(filename):
        questions = []
        with open(filename, 'r', encoding='utf-8') as f:
            for line in f:
                if line == '' or '#' in line: continue
                parts = line.strip().split('|')
                if len(parts) >= 2:
                    question = parts[0]
                    answers = []
                    correct = []
                    for ans in parts[1:]:
                        clean = ans.lstrip('*')
                        answers.append(clean)
                        if ans.startswith('*'):
                            correct.append(clean)
                    random.shuffle(answers)
                    questions.append({
                        'question': question,
                        'answers': answers,
                        'correct': correct
                    })
        return questions

    study_questions = load_questions_from_file(config.gamedir + "\study_game\studygame.txt")

label study_game:
    scene bg studybook
    with dissolve_scene_full
    play music t4
    if persistent.playthrough == 2 and chapter == 2:
        call screen dialog("It's time to study!\n\nPick the correct answer to the questions for a grade at the end!", ok_action=Return())
    
    $ current_index = 0
    $ score = 0
    $ total = len(study_questions)
    $ study = False
    $ quick_menu = False

label study_game_start:
    if current_index >= total:
        jump study_end

    $ q = study_questions[current_index]
    $ question_text = q['question']
    $ answer_choices = q['answers']
    $ correct_answer = q['correct']

    show screen study_question_screen(question_text, answer_choices)

    $ result = ui.interact()

    if result in correct_answer:
        $ score += 1

    $ current_index += 1
    jump study_game_start

screen study_question_screen(question, answers):
    frame:
        background None
        xalign 0.5
        yalign 0.0
        ypos 48
        xsize 1050
        ysize 60
        text question size 40 xalign 0.5 yalign 1

    $ positions = [(0.29, 0.31), (0.71, 0.31), (0.29, 0.56), (0.71, 0.56)]

    for i, ans in enumerate(answers):
        if i < len(positions):
            textbutton ans action Return(ans) xpos positions[i][0] ypos positions[i][1] xanchor 0.5 yanchor 0.5

label study_end:
    hide screen study_question_screen
    centered "Grade: [int((float(score) / total) * 100)]\%"
    $ study = True
    $ config.allow_skipping = True
    $ allow_skipping = True
    $ quick_menu = True

    stop music fadeout 2.0
    show black as fadeout:
        alpha 0
        linear 1.0 alpha 1.0
    pause 1.0
    return
