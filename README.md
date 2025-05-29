# Zeppein Discord Bot

Welcome to the **Zeppein** Discord Bot! 🎉

Zeppein is a powerful and versatile Discord bot designed to enhance your server's moderation and community engagement. With a focus on user management, Zeppein offers a range of commands to help you manage your server efficiently.

## Features

- **Moderation Commands**:
  - Kick users from the server with the `!kick` command.
  - Ban users with the `!ban` command and provide a reason.
  - Unban users using the `!unban` command, just by mentioning their name and discriminator (e.g., `username#1234`).
  - List all banned users with the `!list_bans` command.

- **Logging**:
  - Every moderation action is logged in a dedicated channel (`mod-log`), ensuring transparency and accountability.

## Getting Started

To set up the Zeppein bot on your server, follow these steps:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/oar06g/Zeppein-Discord-Bot.git
   cd Zeppein-Discord-Bot
   ```

2. **Install Dependencies**:
   Make sure you have Python installed, then run:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set Up Environment Variables**:
   Create a `.env` file in the root directory and add your Discord bot token:
   ```
   DISCORD_TOKEN=your_token_here
   ```

4. **Run the Bot**:
   Execute the bot script:
   ```bash
   python bot.py
   ```

## Usage

- Use `!kick @user` to kick a user.
- Use `!ban @user [reason]` to ban a user.
- Use `!unban username#discriminator` to unban a user.
- Use `!list_bans` to view all banned users.

## Contributing

Contributions are welcome! Feel free to submit issues or pull requests. 

## License

This project is licensed under the MIT License.

Thank you for using my project
