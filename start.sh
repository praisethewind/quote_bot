#!/bin/bash
exec screen -dmS quote_bot sh -c 'python bot.py; exec bash'