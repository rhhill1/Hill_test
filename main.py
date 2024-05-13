def on_on_chat():
    # % highlight
    for i in range(100):
        mobs.spawn(CHICKEN, pos(0, 10, 0))
player.on_chat("chicken", on_on_chat)