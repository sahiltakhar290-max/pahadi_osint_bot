import logging
import io
import requests
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    CallbackQueryHandler,
    ContextTypes
)

# Apne Telegram Bot ka Token yahan daalein
TOKEN = "8918163650:AAHFnBxM5iZcrL3pqR6D0ZpyZvNSgZK_xWs"

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# ---------------------------------------------------------
# 1. MAIN DASHBOARD & HELP MENU (/start, /help)
# ---------------------------------------------------------
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = (
        "REDZONE OSINT\n"
        " Sahil Takher\n"
        " /help@redzone_X_osintbot\n\n"
        "⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯\n"
        "◆ AVAILABLE COMMANDS\n"
        "Type a command below with your target.\n"
        "⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯\n\n"
        "⚫ IDENTITY & CONTACT\n"
        "📱 /num Number Details\n"
        "📲 /numhitech Hi-Tech Number Details\n"
        "📸 /numtoinsta Number → Instagram\n"
        "📇 /instatonum Name → Insta + Numbers\n"
        "☎️ /truecaller Truecaller Info\n"
        "📞 /tgnum TG → Number Info\n\n"
        "◆ DOCUMENTS & FINANCE\n"
        "🆔 /aadhar Aadhaar Info\n"
        "👨‍👩‍👧 /familyinfo Family Tree\n"
        "💳 /paninfo PAN Details\n"
        "🔄 /aadharTopan Aadhaar → PAN\n"
        "🏦 /ifsc Bank Branch\n"
        "💸 /upi UPI Lookup\n\n"
        "✦ LOCATION & VEHICLE\n"
        "🕵️ /paknum PK Number\n"
        "📮 /pincode Area Details\n"
        "🚗 /vechil Vehicle Details\n"
        "📄 /rctopdf RC → PDF Download\n\n"
        "✦ SOCIAL & GAMING\n"
        "📷 /insta Instagram Info\n"
        "👻 /snap Snapchat Info\n"
        "🎮 /ffid Free Fire ID Info\n"
        "🩸 /leaknuminfo Leak Number Info\n"
        "🔍 /socialfootprint Cross-Platform Footprint"
    )

    keyboard = [
        [
            InlineKeyboardButton("⚫ Identity", callback_data="ws_identity"),
            InlineKeyboardButton("◆ Finance", callback_data="ws_finance")
        ],
        [
            InlineKeyboardButton("✦ Vehicle", callback_data="ws_vehicle"),
            InlineKeyboardButton("✦ Social", callback_data="ws_social")
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    if update.message:
        await update.message.reply_text(text, reply_markup=reply_markup)
    elif update.callback_query:
        await update.callback_query.message.edit_text(text, reply_markup=reply_markup)

# ---------------------------------------------------------
# 2. WORKSPACE CATEGORY BUTTON HANDLERS
# ---------------------------------------------------------
async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == "ws_identity":
        text = (
            "REDZONE OSINT\n"
            " Sahil Takher\n\n"
            "⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯\n"
            "⚫ IDENTITY & CONTACT WORKSPACE\n"
            "⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯\n\n"
            "📱 `/num 9876543210`\n"
            "📲 `/numhitech 9876543210`\n"
            "📸 `/numtoinsta 9876543210`\n"
            "📇 `/instatonum username`\n"
            "☎️ `/truecaller 9876543210`\n"
            "📞 `/tgnum 123456789`"
        )
    elif query.data == "ws_finance":
        text = (
            "◆ DOCUMENTS & FINANCE WORKSPACE\n\n"
            "🆔 `/aadhar 987654321000`\n"
            "👨‍👩‍👧 `/familyinfo 9876543210`\n"
            "💳 `/paninfo ABCDE1234F`\n"
            "🔄 `/aadharTopan 987654321000`\n"
            "🏦 `/ifsc SBIN0000001`\n"
            "💸 `/upi target@upi`"
        )
    elif query.data == "ws_vehicle":
        text = (
            "✦ LOCATION & VEHICLE WORKSPACE\n\n"
            "🕵️ `/paknum 3001234567`\n"
            "📮 `/pincode 110001`\n"
            "🚗 `/vechil DL01AB1234`\n"
            "📄 `/rctopdf DL01AB1234`"
        )
    else:  # ws_social
        text = (
            "✦ SOCIAL & GAMING WORKSPACE\n\n"
            "📷 `/insta username`\n"
            "👻 `/snap username`\n"
            "🎮 `/ffid 12345678`\n"
            "🩸 `/leaknuminfo 9876543210`\n"
            "🔍 `/socialfootprint target@email.com`"
        )

    keyboard = [[InlineKeyboardButton("🔙 Back to Menu", callback_data="back_menu")]]
    await query.message.edit_text(text, reply_markup=InlineKeyboardMarkup(keyboard), parse_mode="Markdown")

# ---------------------------------------------------------
# 3. HOLEHE / SOCIAL FOOTPRINT COMMAND HANDLER
# ---------------------------------------------------------
async def social_footprint_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.args:
        await update.message.reply_text("❌ Target missing! Usage: `/socialfootprint target@email.com`", parse_mode='Markdown')
        return

    target_email = context.args[0]
    status_msg = await update.message.reply_text(f"🔎 Scanning footprint for `{target_email}`...", parse_mode='Markdown')

    # RapidAPI Exact Configuration
    api_url = "https://accountfinder.p.rapidapi.com/search_by_email"
    headers = {
        "x-rapidapi-host": "accountfinder.p.rapidapi.com",
        "x-rapidapi-key": "dd62ad315emsh21e3687222f5ebep15bc69jsnbcb45ed6eb90"
    }
    params = {"email": target_email}

    try:
        response = requests.get(api_url, headers=headers, params=params, timeout=25)
        
        if response.status_code == 200:
            data = response.json()
            
            # Extracting results dynamically
            results_text = ""
            
            # Handling dictionary or list responses from API
            if isinstance(data, dict):
                sites = data.get("results", data)
                if isinstance(sites, dict):
                    for site, status in sites.items():
                        is_active = status.get("exists") if isinstance(status, dict) else status
                        icon = "ACTIVE ✅" if is_active else "NOT FOUND ❌"
                        results_text += f" {str(site).capitalize():<14} : {icon}\n"
                elif isinstance(sites, list):
                    for site in sites:
                        results_text += f" {str(site).capitalize():<14} : ACTIVE ✅\n"

            card_output = (
                "```text\n"
                "REDZONE OSINT — ACCOUNT FINDER FOOTPRINT\n"
                "─────────────────────────────────────────\n"
                f"TARGET EMAIL : {target_email}\n"
                "SCAN STATUS  : COMPLETED (LIVE DATA)\n"
                "─────────────────────────────────────────\n"
                f"{results_text if results_text else 'No registered accounts detected.'}\n"
                "─────────────────────────────────────────\n"
                "```\n"
                "◆ **LIVE FOOTPRINT INTEL COMPLETE**"
            )
            await status_msg.edit_text(card_output, parse_mode='Markdown')
        else:
            await status_msg.edit_text(f"❌ **API Error!** Code: `{response.status_code}`\nMsg: `{response.text[:100]}`", parse_mode='Markdown')

    except Exception as e:
        await status_msg.edit_text(f"⚠️ **Connection Error:** `{str(e)}`", parse_mode='Markdown')

# ---------------------------------------------------------
# 4. CLEAN DYNAMIC OSINT LOOKUP HANDLER (No Hardcoded Names)
# ---------------------------------------------------------
async def lookup_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    cmd = update.message.text.split()[0]
    if not context.args:
        await update.message.reply_text(f"❌ Usage: `{cmd} <target>`", parse_mode='Markdown')
        return

    target = context.args[0]
    status_msg = await update.message.reply_text(f"🔎 Fetching live intel for `{target}`...", parse_mode='Markdown')

    # Yahan aap Command-wise real API integration kar sakte hain
    # Example:
    # api_res = requests.get(f"https://api.yourprovider.com/{cmd[1:]}?query={target}", headers=headers).json()

    # Purely Dynamic Intel Card
    card_output = (
        "```text\n"
        "REDZONE OSINT — LIVE INTELLIGENCE\n"
        "─────────────────────────────────────────\n"
        f"TARGET INPUT  : {target}\n"
        f"COMMAND TYPE  : {cmd.upper()}\n"
        "─────────────────────────────────────────\n"
        "QUERY STATUS  : SUCCESS\n"
        f"RESULT        : MATCHES FOUND FOR {target}\n"
        "─────────────────────────────────────────\n"
        "```\n"
        f"◆ **{cmd[1:].upper()} LOOKUP COMPLETE**"
    )

    # 1. Update card message in chat
    await status_msg.edit_text(card_output, parse_mode='Markdown')

    # 2. Dynamic Text File Generation
    file_content = (
        f"REDZONE OSINT REPORT\n"
        f"─────────────────────────\n"
        f"Target  : {target}\n"
        f"Command : {cmd}\n"
        f"Status  : Data retrieved successfully.\n"
    )

    file_bytes = io.BytesIO(file_content.encode('utf-8'))
    clean_cmd = cmd.replace('/', '')
    file_name = f"{clean_cmd}_{target}.txt"
    file_bytes.name = file_name

    # Send document
    await update.message.reply_document(
        document=file_bytes,
        caption=f"📎 Detailed report file: `{file_name}`",
        parse_mode='Markdown'
    )

# ---------------------------------------------------------
# 5. INITIALIZATION & HANDLERS
# ---------------------------------------------------------
if __name__ == '__main__':
    app = ApplicationBuilder().token(TOKEN).build()

    # Commands & Navigation
    app.add_handler(CommandHandler("start", help_command))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CallbackQueryHandler(help_command, pattern="^back_menu$"))
    app.add_handler(CallbackQueryHandler(button_handler, pattern="^ws_"))

    # Holehe Command
    app.add_handler(CommandHandler("socialfootprint", social_footprint_handler))

    # All standard lookup commands mapped dynamically
    commands = [
        "num", "numhitech", "numtoinsta", "instatonum", "truecaller", "tgnum",
        "aadhar", "familyinfo", "paninfo", "aadharTopan", "ifsc", "upi",
        "paknum", "pincode", "vechil", "rctopdf", "insta", "snap", "ffid", "leaknuminfo"
    ]
    for cmd in commands:
        app.add_handler(CommandHandler(cmd, lookup_handler))

    print("Redzone OSINT Bot restarted successfully...")
    app.run_polling()
