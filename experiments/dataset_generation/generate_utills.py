from config import LOGIC_RULE_TEMPLATES
import random

def create_question(template, params):
    question = {
        'context': template['context'].format(**params),
        'qa_pairs': [
            {"question": pair['question'].format(**params),
             "answer": pair['answer']}
            for pair in template['qa_pairs']
        ]
    }
    return question


def generate_cause_consequence_questions_from_template(template, grouped_causes_female, grouped_causes_male, consequences_female, consequences_male, names_female, names_male):
    questions_male = []
    questions_female = []
    for group, group_causes in grouped_causes_male.items():
        number_of_names = min(len(names_male), len(group_causes)*len(consequences_male[group]) // 10)
        for cause in group_causes:
            for consequence in consequences_male[group]:
                for name in random.sample(names_male, number_of_names):
                    params = {
                        'cause': cause,
                        'cause_male': cause,
                        'consequence': consequence,
                        'consequence_male': consequence,
                        'name': name,
                        'pronoun': 'він'
                    }
                    question = create_question(template, params)
                    questions_male.append(question)
    for group, group_causes in grouped_causes_female.items():
        number_of_names = min(len(names_female), len(group_causes)*len(consequences_female[group]) // 10)
        for i in range(len(group_causes)):
            cause = group_causes[i]
            cause_male = grouped_causes_male[group][i]
            for j in range(len(consequences_female[group])):
                consequence = consequences_female[group][j]
                consequence_male = consequences_male[group][j]
                for name in random.sample(names_female, number_of_names):
                    params = {
                        'cause': cause,
                        'cause_male': cause_male,
                        'consequence': consequence,
                        'consequence_male': consequence_male,
                        'name': name,
                        'pronoun': 'вона'
                    }
                    question = create_question(template, params)
                    questions_female.append(question)
    return {'male_questions': questions_male, 'female_questions': questions_female}


def generate_select_true_fact_questions_from_template(template, facts, names):
    questions = []
    for fact1 in facts:
        for fact2 in facts:
            if fact1 == fact2:
                continue
            number_of_names = min(len(names), 2)
            names_sample = random.sample(names, number_of_names)
            for i in range(number_of_names - 1):
                params = {
                    'fact1': fact1,
                    'fact2': fact2,
                    'name1': names_sample[i],
                    'name2': names_sample[i+1]
                }
                question = create_question(template, params)
                questions.append(question)
    return questions

def generate_constructive_dilemma_questions_from_template(template, grouped_causes_female, grouped_causes_male,
                                                          consequences_female, consequences_male, names_female, names_male):
    questions_male = []
    questions_female = []
    for group1, group_causes1 in grouped_causes_male.items():
        for group2, group_causes2 in grouped_causes_male.items():
            if group1 == group2:
                continue
            for cause1 in group_causes1:
                for consequence1 in consequences_male[group1]:
                    for name in names_male:
                        params = {
                            'cause1': cause1,
                            'cause_male1': cause1,
                            'consequence1': consequence1,
                            'consequence_male1': consequence1,
                            'cause2': group_causes2[0],
                            'cause_male2': group_causes2[0],
                            'consequence2': consequences_male[group2][0],
                            'consequence_male2': consequences_male[group2][0],
                            'name': name,
                            'pronoun': 'він'
                        }
                        question = create_question(template, params)
                        questions_male.append(question)
    for group1, group_causes1 in grouped_causes_female.items():
        for group2, group_causes2 in grouped_causes_female.items():
            if group1 == group2:
                continue
            for i in range(len(group_causes1)):
                cause1 = group_causes1[i]
                cause_male1 = grouped_causes_male[group1][i]
                for j in range(len(consequences_female[group1])):
                    consequence1 = consequences_female[group1][j]
                    consequence_male1 = consequences_male[group1][j]
                    for name in names_female:
                        params = {
                            'cause1': cause1,
                            'cause_male1': cause_male1,
                            'consequence1': consequence1,
                            'consequence_male1': consequence_male1,
                            'cause2': group_causes2[0],
                            'cause_male2': grouped_causes_male[group2][0],
                            'consequence2': consequences_female[group2][0],
                            'consequence_male2': consequences_male[group2][0],
                            'name': name,
                            'pronoun': 'вона'
                        }
                        question = create_question(template, params)
                        questions_female.append(question)
    return {'male_questions': questions_male, 'female_questions': questions_female}


def generate_questions_from_cause_consequence_templates(grouped_causes_female, grouped_causes_male, consequences_female, consequences_male, names_female, names_male):
    questions = {}
    for rule  in LOGIC_RULE_TEMPLATES:
        template = LOGIC_RULE_TEMPLATES[rule]
        if template['question_type'] == 'cause_consequence':
            questions[rule] =  generate_cause_consequence_questions_from_template(template, grouped_causes_female, grouped_causes_male,
                                                                      consequences_female, consequences_male, names_female, names_male)
        elif template['question_type'] == 'con/destructive_dilemma':
            questions[rule] = generate_constructive_dilemma_questions_from_template(template, grouped_causes_female, grouped_causes_male,
                                                                                    consequences_female, consequences_male, names_female, names_male)
        else:
            pass
        print(f"Generating questions for {rule} rule")

    return questions

def generate_questions_from_select_true_fact_templates(facts, names):
    questions = {}
    for rule  in LOGIC_RULE_TEMPLATES:
        template = LOGIC_RULE_TEMPLATES[rule]
        if template['question_type'] == 'select_true_fact':
            questions[rule] =  generate_select_true_fact_questions_from_template(template, facts, names)
            print(f"Generating questions for {rule} rule")
        else:
            pass
    return questions