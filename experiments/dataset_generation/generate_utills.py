from config import LOGIC_RULE_TEMPLATES

def create_question(template, cause, cause_male, consequence, consequence_male, name, pronoun):
    question = {
        'context': template['context'].format(cause_male=cause_male, consequence_male=consequence_male),
        'qa_pairs': [
            {"question": pair['question'].format(name=name, cause=cause, consequence=consequence, pronoun=pronoun),
             "answer": pair['answer']}
            for pair in template['qa_pairs']
        ]
    }
    return question


def generate_questions_from_template(template, grouped_causes_female, grouped_causes_male, consequences_female, consequences_male, names_female, names_male):
    questions_male = []
    questions_female = []
    for group, group_causes in grouped_causes_male.items():
        for cause in group_causes:
            for consequence in consequences_male[group]:
                for name in names_male:
                    question = create_question(template, cause, cause, consequence, consequence, name, 'він')
                    questions_male.append(question)
    for group, group_causes in grouped_causes_female.items():
        for i in range(len(group_causes)):
            cause = group_causes[i]
            cause_male = grouped_causes_male[group][i]
            for j in range(len(consequences_female[group])):
                consequence = consequences_female[group][j]
                consequence_male = consequences_male[group][j]
                for name in names_female:
                    question = create_question(template, cause, cause_male, consequence, consequence_male, name, 'вона')
                    questions_female.append(question)
    return {'male_questions': questions_male, 'female_questions': questions_female}


def generate_questions_according_to_logic_rule(grouped_causes_female, grouped_causes_male, consequences_female, consequences_male, names_female, names_male, rule):
    if rule not in LOGIC_RULE_TEMPLATES:
        print(f"Rule {rule} is not supported. Choose one of the following: {LOGIC_RULE_TEMPLATES.keys()}")
    else:
        template = LOGIC_RULE_TEMPLATES[rule]
        return generate_questions_from_template(template, grouped_causes_female, grouped_causes_male,
                                                consequences_female, consequences_male, names_female, names_male)
