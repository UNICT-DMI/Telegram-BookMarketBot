def start(update, context):
    chat_id = update.effective_chat.id
    context.bot.send_message(chat_id, "Ciao! Con questo bot puoi mettere in vendita i tuoi libri usati e comprare libri che altri colleghi non utilizzano più. Per maggiori informazioni utilizza il comando /help")