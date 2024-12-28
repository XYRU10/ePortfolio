from graphviz import Digraph

def caesar_dfa_graph(shift=3):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    dot = Digraph(comment="Caesar Cipher DFA")
    
    # Add nodes (states)
    for letter in alphabet:
        dot.node(letter, f"q_{letter}")  # State names
    
    # Add transitions (directed edges)
    for letter in alphabet:
        current_state = letter
        next_state = alphabet[(alphabet.index(letter) + shift) % 26]
        dot.edge(current_state, next_state, label=f"{letter} → {next_state}")
    
    # Render and save the graph
    dot.render('caesar_cipher_dfa', format='png', cleanup=True)
    print("Graph generated as 'caesar_cipher_dfa.png'")

# Generate the graph
caesar_dfa_graph(shift=3)
