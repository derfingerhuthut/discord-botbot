import discord
from discord.ext import commands
from discord import app_commands
import random
import asyncio

# ── Bot Setup ──────────────────────────────────────────────────────────────────
intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix="!", intents=intents)

# ── Data ───────────────────────────────────────────────────────────────────────
FACTS = [
    "Honey never spoils. Archaeologists have found 3,000-year-old honey in Egyptian tombs that was still edible.",
    "A group of flamingos is called a 'flamboyance'.",
    "Octopuses have three hearts and blue blood.",
    "The Eiffel Tower grows about 15 cm taller in summer due to thermal expansion.",
    "A single strand of spaghetti is called a 'spaghetto'.",
    "Crows can recognize and remember human faces.",
    "The shortest war in history lasted only 38–45 minutes (Anglo-Zanzibar War, 1896).",
    "Bananas are berries, but strawberries are not.",
    "A day on Venus is longer than a year on Venus.",
    "Sharks are older than trees — they've existed for over 400 million years.",
    "The average person walks about 100,000 miles in their lifetime.",
    "Wombat poop is cube-shaped.",
    "A bolt of lightning is five times hotter than the surface of the sun.",
    "Cleopatra lived closer in time to the Moon landing than to the construction of the Great Pyramid.",
    "Sea otters hold hands while sleeping so they don't drift apart.",
    "The unicorn is the national animal of Scotland.",
    "Humans share 60% of their DNA with bananas.",
    "The word 'nerd' was first used by Dr. Seuss in 'If I Ran the Zoo' (1950).",
    "There are more possible iterations of a game of chess than atoms in the observable universe.",
    "A snail can sleep for up to three years.",
]

ADJECTIVES = [
    "Shadow", "Neon", "Cosmic", "Blazing", "Silent", "Frozen", "Mystic",
    "Rogue", "Quantum", "Phantom", "Crystal", "Iron", "Storm", "Void",
    "Hyper", "Stealth", "Turbo", "Cyber", "Lunar", "Solar",
]

NOUNS = [
    "Wolf", "Blade", "Hawk", "Phoenix", "Viper", "Echo", "Titan",
    "Ghost", "Fox", "Drake", "Raven", "Storm", "Comet", "Nova",
    "Specter", "Falcon", "Wraith", "Panda", "Lynx", "Kraken",
]

SUFFIXES = ["42", "99", "XD", "_Pro", "777", "_OG", "404", "exe", "_v2", ""]

GAMES = [
    {"title": "Hollow Knight", "genre": "Metroidvania", "desc": "A challenging and atmospheric insect-kingdom adventure."},
    {"title": "Stardew Valley", "genre": "Farming Sim / RPG", "desc": "Build your farm, make friends, explore mines. Endlessly relaxing."},
    {"title": "Celeste", "genre": "Platformer", "desc": "A tight platformer about climbing a mountain — and mental health."},
    {"title": "Terraria", "genre": "Sandbox / Action", "desc": "2D Minecraft meets action RPG with hundreds of hours of content."},
    {"title": "Outer Wilds", "genre": "Exploration / Mystery", "desc": "A solar system stuck in a time loop. One of the best mysteries in gaming."},
    {"title": "Disco Elysium", "genre": "RPG", "desc": "A deeply written detective RPG unlike anything else."},
    {"title": "Hades", "genre": "Roguelike", "desc": "Escape the Underworld with tight combat and great storytelling."},
    {"title": "Deep Rock Galactic", "genre": "Co-op Shooter", "desc": "Mine, shoot bugs, drink beer with friends. Rock and Stone!"},
    {"title": "Risk of Rain 2", "genre": "Roguelike Shooter", "desc": "Third-person roguelike with escalating chaos and great loot."},
    {"title": "Subnautica", "genre": "Survival / Exploration", "desc": "Crash-land on an ocean planet and survive the depths below."},
    {"title": "Portal 2", "genre": "Puzzle", "desc": "Mind-bending puzzle game with one of gaming's best narratives."},
    {"title": "Valheim", "genre": "Survival / Co-op", "desc": "Viking survival sandbox with gorgeous procedural worlds."},
    {"title": "Into the Breach", "genre": "Turn-based Strategy", "desc": "Perfect, tight tactical puzzles defending cities from giant bugs."},
    {"title": "Phasmophobia", "genre": "Horror / Co-op", "desc": "Investigate hauntings with friends. Terrifying in all the right ways."},
    {"title": "Noita", "genre": "Roguelike / Sandbox", "desc": "Every pixel is simulated. Magic wands, explosions, pure chaos."},
]


# ── /fact ──────────────────────────────────────────────────────────────────────
@bot.tree.command(name="fact", description="Get a random interesting fact!")
async def fact(interaction: discord.Interaction):
    chosen = random.choice(FACTS)
    embed = discord.Embed(
        title="🧠 Random Fact",
        description=chosen,
        color=discord.Color.teal()
    )
    await interaction.response.send_message(embed=embed)


# ── /username ──────────────────────────────────────────────────────────────────
@bot.tree.command(name="username", description="Generate a random cool username!")
async def username(interaction: discord.Interaction):
    name = random.choice(ADJECTIVES) + random.choice(NOUNS) + random.choice(SUFFIXES)
    embed = discord.Embed(
        title="🎮 Username Generator",
        description=f"How about: **`{name}`**?",
        color=discord.Color.purple()
    )
    embed.set_footer(text="Run /username again for a new one!")
    await interaction.response.send_message(embed=embed)


# ── /game ──────────────────────────────────────────────────────────────────────
@bot.tree.command(name="game", description="Get a random game recommendation!")
async def game(interaction: discord.Interaction):
    pick = random.choice(GAMES)
    embed = discord.Embed(
        title=f"🎲 You should play: **{pick['title']}**",
        description=pick["desc"],
        color=discord.Color.orange()
    )
    embed.add_field(name="Genre", value=pick["genre"], inline=True)
    embed.set_footer(text="Run /game again for another recommendation!")
    await interaction.response.send_message(embed=embed)


# ── /dm ────────────────────────────────────────────────────────────────────────
@bot.tree.command(name="dm", description="Send a DM to a server member.")
@app_commands.describe(member="The user to DM", message="The message to send")
async def dm(interaction: discord.Interaction, member: discord.Member, message: str):
    if member.bot:
        await interaction.response.send_message("❌ You can't DM a bot.", ephemeral=True)
        return
    try:
        embed = discord.Embed(
            title="📬 New Message",
            description=message,
            color=discord.Color.blurple()
        )
        embed.set_footer(text=f"Sent by {interaction.user} from {interaction.guild.name}")
        await member.send(embed=embed)
        await interaction.response.send_message(
            f"✅ DM sent to **{member.display_name}**!", ephemeral=True
        )
    except discord.Forbidden:
        await interaction.response.send_message(
            f"❌ Couldn't DM **{member.display_name}** — they may have DMs disabled.", ephemeral=True
        )


# ── /tictactoe ─────────────────────────────────────────────────────────────────
class TicTacToeButton(discord.ui.Button):
    def __init__(self, row: int, col: int):
        super().__init__(style=discord.ButtonStyle.secondary, label="\u200b", row=row)
        self.row_pos = row
        self.col_pos = col

    async def callback(self, interaction: discord.Interaction):
        view: TicTacToeView = self.view
        game = view.game

        if interaction.user not in (game.player_x, game.player_o):
            await interaction.response.send_message("❌ You're not in this game!", ephemeral=True)
            return

        current_player = game.player_x if game.current == "X" else game.player_o
        if interaction.user != current_player:
            await interaction.response.send_message("⏳ It's not your turn!", ephemeral=True)
            return

        if game.board[self.row_pos][self.col_pos] != " ":
            await interaction.response.send_message("❌ That cell is already taken!", ephemeral=True)
            return

        game.board[self.row_pos][self.col_pos] = game.current
        self.label = "❌" if game.current == "X" else "⭕"
        self.style = discord.ButtonStyle.danger if game.current == "X" else discord.ButtonStyle.primary
        self.disabled = True

        winner = game.check_winner()
        if winner:
            for child in view.children:
                child.disabled = True
            win_player = game.player_x if winner == "X" else game.player_o
            embed = discord.Embed(
                title="🏆 Tic Tac Toe — Game Over!",
                description=f"**{win_player.display_name}** wins as {'❌' if winner == 'X' else '⭕'}!",
                color=discord.Color.gold()
            )
            await interaction.response.edit_message(embed=embed, view=view)
        elif game.is_draw():
            for child in view.children:
                child.disabled = True
            embed = discord.Embed(
                title="🤝 Tic Tac Toe — Draw!",
                description="No more moves left. It's a draw!",
                color=discord.Color.greyple()
            )
            await interaction.response.edit_message(embed=embed, view=view)
        else:
            game.current = "O" if game.current == "X" else "X"
            next_player = game.player_x if game.current == "X" else game.player_o
            symbol = "❌" if game.current == "X" else "⭕"
            embed = discord.Embed(
                title="🎮 Tic Tac Toe",
                description=f"Turn: **{next_player.display_name}** ({symbol})",
                color=discord.Color.green()
            )
            await interaction.response.edit_message(embed=embed, view=view)


class TicTacToeGame:
    def __init__(self, player_x: discord.Member, player_o: discord.Member):
        self.player_x = player_x
        self.player_o = player_o
        self.board = [[" "] * 3 for _ in range(3)]
        self.current = "X"

    def check_winner(self):
        b = self.board
        lines = (
            [b[r] for r in range(3)]          # rows
            + [[b[r][c] for r in range(3)] for c in range(3)]  # cols
            + [[b[0][0], b[1][1], b[2][2]]]   # diag
            + [[b[0][2], b[1][1], b[2][0]]]   # anti-diag
        )
        for line in lines:
            if line[0] != " " and all(c == line[0] for c in line):
                return line[0]
        return None

    def is_draw(self):
        return all(cell != " " for row in self.board for cell in row)


class TicTacToeView(discord.ui.View):
    def __init__(self, game: TicTacToeGame):
        super().__init__(timeout=300)
        self.game = game
        for row in range(3):
            for col in range(3):
                self.add_item(TicTacToeButton(row, col))


@bot.tree.command(name="tictactoe", description="Challenge someone to a game of Tic Tac Toe!")
@app_commands.describe(opponent="The member you want to challenge")
async def tictactoe(interaction: discord.Interaction, opponent: discord.Member):
    if opponent == interaction.user:
        await interaction.response.send_message("❌ You can't play against yourself!", ephemeral=True)
        return
    if opponent.bot:
        await interaction.response.send_message("❌ You can't challenge a bot!", ephemeral=True)
        return

    game = TicTacToeGame(player_x=interaction.user, player_o=opponent)
    view = TicTacToeView(game)

    embed = discord.Embed(
        title="🎮 Tic Tac Toe",
        description=(
            f"**{interaction.user.display_name}** (❌) vs **{opponent.display_name}** (⭕)\n\n"
            f"Turn: **{interaction.user.display_name}** (❌)"
        ),
        color=discord.Color.green()
    )
    await interaction.response.send_message(embed=embed, view=view)


# ── Ready & Sync ───────────────────────────────────────────────────────────────
@bot.event
async def on_ready():
    await bot.tree.sync()
    print(f"✅ Logged in as {bot.user} (ID: {bot.user.id})")
    print("Slash commands synced. Bot is ready!")


# ── Run ────────────────────────────────────────────────────────────────────────
bot.run(os.getenv("DISCORD_TOKEN"))
