from content.quiz_content import Question, Answer

def test_create_answer():
    from_csv = {'id': '37', 'text': 'The Deputy Director', 'question_id': '15', 'is_correct': 'FALSE'}
    answer = Answer(from_csv['id'], from_csv['text'], from_csv['question_id'], from_csv['is_correct'])

    assert answer.id == 37
    assert answer.text == 'The Deputy Director'
    assert answer.question_id == 15
    assert answer.is_correct == False

def test_create_question():
    from_csv = {'id': '15', 
               'text': 'Who needs to be informed if the Plan Tech experiences an outage?', 
               'answer_ids': '37,38,39', 
               'discipline': 'Product and Delivery', 
               'wiki_topic': '        Disaster recovery               ', 
               'wiki_href': 'https://www.get-help-buying-for-schools.service.gov.uk/procurement-support', 
               'advice_text': 'You (or another member of the team) should alert the Service Owner and Service Delivery Manager, and ensure there is a ServiceNow incident ticket raised.'} 

    question = Question(from_csv['id'], from_csv['text'], from_csv['answer_ids'], from_csv['discipline'], from_csv['wiki_topic'], from_csv['wiki_href'], from_csv['advice_text'])
    
    assert question.id == 15
    assert question.text == 'Who needs to be informed if the Plan Tech experiences an outage?'
    assert question.answer_ids == [37,38,39]
    assert question.discipline == 'Product and Delivery'
    assert question.wiki_topic == 'Disaster recovery'
    assert question.wiki_href == 'https://www.get-help-buying-for-schools.service.gov.uk/procurement-support'
    assert question.advice_text == 'You (or another member of the team) should alert the Service Owner and Service Delivery Manager, and ensure there is a ServiceNow incident ticket raised.'
    