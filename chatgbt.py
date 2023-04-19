from flask import Flask, jsonify, request
from chatgpt_wrapper import ChatGPT

app = Flask(__name__)
bot = ChatGPT()

@app.route('/chatbot', methods=['POST'])
def chatbot():
    dua_string = request.json.get('dua_string')
    question = "The first word in your answer should be Yes or No. Does the following DUA default to jurisdictional laws in the event that a clause of the DUA violates one: "
    question+=dua_string
    response = bot.ask(question)
    words = response[1].split()
    if words[0].lower() == "no." or words[0]=="no" or words[0]=="no,":
        return jsonify({'result': [False, False]})
    elif words[0].lower()=="yes" or words[0].lower()=="yes." or words[0].lower()=="yes,":
        return jsonify({'result': [True, True]})
    else:
        return jsonify({'error': 'chatgpt failed to provide yes or no answer'})

if __name__ == '__main__':
    app.run(debug=True)

#print(chatbot("Miscellaneous.  Recipient and Mayo agree that individuals whose Protected Health Information appears in a Limited Data Set are not third-party beneficiaries of this Agreement.  In the event that any provision of this Agreement violates any applicable statute, ordinance or rule of law in any jurisdiction that governs this Agreement, such provision shall be ineffective to the extent of such violation without invalidating any other provision of this Agreement.  This Agreement may not be amended, altered or modified except by written agreement signed by Recipient and Mayo.  No provision of this Agreement may be waived except by an agreement in writing signed by the waiving party.  A waiver of any term or provision shall not be construed as a waiver of any other term or provision.  Nothing in Section 3 of this Agreement shall be deemed a waiver of any legally-recognized claim of privilege available to Recipient.  The persons signing below have the right and authority to execute this Agreement for their respective entities and no further approvals are necessary to create a binding agreement.  Neither Mayo nor Recipient shall use the names or trademarks of the other party or of any of the respective party’s affiliated entities in any advertising, publicity, endorsement, or promotion unless prior written consent has been obtained for the particular use contemplated.  All references herein to specific statutes, codes or regulations shall be deemed to be references to those statutes, codes or regulations as may be amended from time to time."))
