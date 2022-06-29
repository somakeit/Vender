# Document = https://wiki.nottinghack.org.uk/images/d/d2/MDB_3.0.pdf # Note: Page 100
from enum import Enum


class Response(Enum):
    JUST_RESET = 0x00
    READER_CONFIG_DATA = 0x01
    DISPLAY_REQUEST = 0x02
    BEGIN_SESSION = 0x03
    SESSION_CANCEL_REQUEST = 0x04
    VEND_APPROVED = 0x05
    VEND_DENIED = 0x06
    END_SESSION = 0x07
    CANCELLED = 0x08
    PERIPHERAL_ID = 0x09
    MALFUNCTION_ERROR = 0x0A
    CMD_OUT_OF_SEQUENCE = 0x0B
    ACKNOWLEDGE = 0x00
    NOT_ACKNOWLEDGED = 0xFF

    def __bytes__(self):
        return bytes(self.value)

    @property
    def hex(self):
        return hex(self.value)

# 00H - Just Reset
# 01H - Reader Config Data
# 02H - Display Request
# 03H - Begin Session
# 04H - Session Cancel
# Request
# 05H - Vend Approved
# 06H - Vend Denied
# 07H - End Session
# 08H - Cancelled
# 09H - Peripheral ID
# 0AH - Malfunction / Error
# 0BH - Cmd Out Of
# Sequence

if __name__ == '__main__':
    print(Response.ACKNOWLEDGE.hex)