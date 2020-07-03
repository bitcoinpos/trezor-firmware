class ProtocolMagics:
    # todo: GK - set mainnet protocol magic (we don't know this value yet)
    MAINNET = 0
    TESTNET = 42

    @classmethod
    def to_ui_string(cls, value: int) -> str:
        ui_string_map = {
            cls.MAINNET: "Mainnet",
            cls.TESTNET: "Testnet",
        }

        return ui_string_map.get(value, "Unknown")
