from loto_class import Compare_Balls, get_user_numbers

def test_get_user_numbers_valid_input(monkeypatch):
    # Use monkeypatch to simulate user input
    monkeypatch.setattr('builtins.input', lambda _: '5,10,15,20,25')
    
    user_numbers = get_user_numbers()
    assert user_numbers == [5, 10, 15, 20, 25]

