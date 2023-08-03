from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackContext, CallbackQueryHandler
from web3 import Web3
from getpass import getpass

# Connect to Ethereum node
w3 = Web3(Web3.HTTPProvider('http://localhost:8545'))  # replace with your node URL

# Contract setup
contract_address = '0x39bab416b63f8d7ffa1d487bd3768ba2dab3330c'  # replace with your contract address
contract_abi = ''  # replace with your contract ABI
contract = w3.eth.contract(address=contract_address, abi=contract_abi)

# Telegram bot setup
updater = Updater(token='YOUR_TELEGRAM_BOT_TOKEN', use_context=True)
dispatcher = updater.dispatcher

def stake(update: Update, context: CallbackContext):
    # This function will be called when the /stake command is issued

    # Get the amount to stake from the command arguments
    amount = int(context.args[0])

    # Call the contract function
    tx_hash = contract.functions.depositAndStakeNeutraUsdc('0xRecipientAddress', amount).transact()

    # Send a message to the user with the transaction hash
    update.message.reply_text(f'Success! Transaction hash: {tx_hash.hex()}')

def redeem(update: Update, context: CallbackContext):
    # This function will be called when the /redeem command is issued

    # Get the amount to redeem from the command arguments
    amount = int(context.args[0])

    # Call the contract function
    tx_hash = contract.functions.unstakeAndRedeemNeutraUsdc('0xRecipientAddress', amount, 0).transact()

    # Send a message to the user with the transaction hash
    update.message.reply_text(f'Success! Transaction hash: {tx_hash.hex()}')

# Add the command handlers to the dispatcher
dispatcher.add_handler(CommandHandler('stake', stake))
dispatcher.add_handler(CommandHandler('redeem', redeem))

updater.start_polling()
