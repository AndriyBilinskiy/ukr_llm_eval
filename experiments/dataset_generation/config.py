LOGIC_RULE_TEMPLATES = {
    'modus_ponens': {
        'question_type': 'cause_consequence',
        'context': "Якщо хтось {cause_male}, тоді він {consequence_male}.",
        'qa_pairs': [
            {"question": "Якщо {name} {cause}, це означає, що {pronoun} {consequence}?", "answer": "так"},
            {"question": "Якщо {name} {cause}, це означає, що {pronoun} не {consequence}?", "answer": "ні"},
            {"question": "Якщо {name} не {cause}, це означає, що {pronoun} {consequence}?", "answer": "ні"},
            {"question": "Якщо {name} не {cause}, це означає, що {pronoun} не {consequence}?", "answer": "ні"}
        ]
    },
    'modus_tollens': {
        'question_type': 'cause_consequence',
        'context': "Якщо хтось {cause_male}, тоді він {consequence_male}.",
        'qa_pairs': [
            {"question": "Якщо {name} не {consequence}, це означає, що {pronoun} не {cause}?", "answer": "так"},
            {"question": "Якщо {name} не {consequence}, це означає, що {pronoun} {cause}?", "answer": "ні"},
            {"question": "Якщо {name} {consequence}, це означає, що {pronoun} {cause}?", "answer": "ні"},
            {"question": "Якщо {name} {consequence}, це означає, що {pronoun} не {cause}?", "answer": "ні"}
        ]
    },
    'material_implication': {
        'question_type': 'cause_consequence',
        'context': "Якщо хтось {cause_male}, тоді він {consequence_male}.",
        'qa_pairs': [
            {"question": "Враховуючи контекст, чи можна зробити висновок, що хоча б одне з наступних тверджень завжди є правдивим? 1. {name} не {cause}, 2. {pronoun} {consequence}?", "answer": "так"},
            {"question": "Враховуючи контекст, чи можна зробити висновок, що хоча б одне з наступних тверджень завжди є правдивим? 1. {name} не {cause}, 2. {pronoun} не {consequence}?", "answer": "так"},
            {"question": "Враховуючи контекст, чи можна зробити висновок, що хоча б одне з наступних тверджень завжди є правдивим? 1. {name} {cause}, 2. {pronoun} {consequence}?", "answer": "ні"},
            {"question": "Враховуючи контекст, чи можна зробити висновок, що хоча б одне з наступних тверджень завжди є правдивим? 1. {name} {cause}, 2. {pronoun} не {consequence}?", "answer": "так"}
        ]
    },
    'disjunctive_syllogism': {
        'question_type': 'select_true_fact',
        'context':'Хоча б одне з наступних тверджень є правдивим: 1. {name1} {fact1}, 2. {name2} {fact2}. Правдивим може бути як один з цих фактів, так і два факти одночасно.',
        'qa_pairs': [
            {"question": "Якщо {name1} не {fact1} чи означає це, що {name2} {fact2}?", "answer": "так"},
            {"question": "Якщо {name1} не {fact1} чи означає це, що {name2} не {fact2}?", "answer": "так"},
            {"question": "Якщо {name1} {fact1} чи означає це, що {name2} не {fact2}?", "answer": "ні"},
            {"question": "Якщо {name1} {fact1} чи означає це, що {name2} {fact2}?", "answer": "ні"}
        ]
    },
    'constructive_dillema': {
        'question_type': 'constructive_dillema',
        'context': "Якщо хтось {cause_male1}, тоді він {consequence_male1}. Якщо хтось {cause_male2}, тоді він {consequence_male2}. Хоча б одне з наступних тверджень є правдивим: 1. {name} {cause1}, 2. {name} {cause2}. Правдивим може бути як один з цих фактів, так і два факти одночасно.",
        'qa_pairs': [
            {"question": "Враховуючи контекст, чи можна зробити висновок, що хоча б одне з наступних тверджень завжди є правдивим? 1. {name} {consequence1}, 2. {pronoun} {consequence2}?", "answer": "так"},
            {"question": "Враховуючи контекст, чи можна зробити висновок, що хоча б одне з наступних тверджень завжди є правдивим? 1. {name} не {consequence1}, 2. {pronoun} {consequence2}?", "answer": "ні"},
            {"question": "Враховуючи контекст, чи можна зробити висновок, що хоча б одне з наступних тверджень завжди є правдивим? 1. {name} не {consequence1}, 2. {pronoun} не {consequence2}?", "answer": "ні"},
            {"question": "Враховуючи контекст, чи можна зробити висновок, що хоча б одне з наступних тверджень завжди є правдивим? 1. {name} {consequence1}, 2. {pronoun} не {consequence2}?", "answer": "ні"},

        ]
    },
}