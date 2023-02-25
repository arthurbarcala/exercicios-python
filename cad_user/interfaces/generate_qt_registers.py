from functions.verify_qt_register import verify_qt_register

def generate_qt_registers() -> None:
    print(f"Quantidade de usuários registrados: {verify_qt_register()}")