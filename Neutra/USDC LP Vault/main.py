import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackContext, CallbackQueryHandler
from web3 import Web3
from getpass import getpass

TELEGRAM_TOKEN = os.environ['Telegram_token']

# Connect to Arbitrum node
w3 = Web3(Web3.HTTPProvider(os.environ['RPC']))  # replace with your node URL environment variable

# Contract setup
contract_address = os.environ['Contract Address']  # replace with your contract address environment variable
# contract_abi = ''  # replace with your contract ABI
# contract = w3.eth.contract(address=contract_address, abi=contract_abi)

# Telegram bot setup
updater = Updater(TELEGRAM_TOKEN, use_context=True)
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
