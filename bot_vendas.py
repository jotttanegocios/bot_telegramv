from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler

# Comando /start
async def start(update: Update, context):
    keyboard = [
        [InlineKeyboardButton("🔞 Ver Conteúdo", callback_data="comprar")]
    ]
    await update.message.reply_text(
        "👋 Oii, vem me ver daquele jeitinho amor🔥😈\nEscolha uma opção para adquirir meu conteúdo exclusivo:",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )

# Quando o botão é clicado
async def button_click(update: Update, context):
    query = update.callback_query
    await query.answer()

    if query.data == "comprar":
        await query.edit_message_text(
            text="💳 Selecione o valor para acessar o conteúdo:\n\n1. R$50 - Pacote Bronze\n2. R$100 - Pacote Prata\n3. R$200 - Pacote Ouro",
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("R$50", callback_data="pagar_50"),
                 InlineKeyboardButton("R$100", callback_data="pagar_100")],
                [InlineKeyboardButton("R$200", callback_data="pagar_200")]
            ])
        )

# Configuração do Bot
app = ApplicationBuilder().token("7533268315:AAFPPhS0_o0XWXN8l_KWk5l5tyQlpfmOoYE").build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CallbackQueryHandler(button_click))

# Executar o bot
app.run_polling()
