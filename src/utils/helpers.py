from utils.db import Database

def display_game_history():
    """Display history of all games played"""
    db = Database()
    cursor = db.conn.cursor()
    cursor.execute("""
        SELECT p.name, p.symbol, COUNT(*) as wins
        FROM games g
        JOIN players p ON p.id = g.winner_id
        GROUP BY p.id
        ORDER BY wins DESC
    """)
    
    print("\nGame History:")
    print("-" * 40)
    for name, symbol, wins in cursor.fetchall():
        print(f"{name} ({symbol}): {wins} wins")
    print("-" * 40)