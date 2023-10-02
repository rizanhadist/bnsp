def pembayaran(total_belanja, uang_dibayar):
    """
    A function to calculate the change based on the total shopping amount and the paid amount.
    
    Parameters:
    - total_belanja: The total amount of shopping.
    - uang_dibayar: The amount of money paid by the customer.
    
    Returns:
    - kembalian: The change to be returned to the customer.
    """
    
    if uang_dibayar < total_belanja:
        print("Uang tidak cukup!")
        return None

    kembalian = uang_dibayar - total_belanja
    return kembalian

# Test the function
total = input("\nTotal pembelanjaan anda : ")
uang = input("\nUang yang Anda ingin bayarkan: ")
# total = 50000  # Example total bill
# uang = 60000   # Example paid money
kembalian = pembayaran(int(total), int(uang))

if kembalian is not None:
    print(f"\nKembalian Anda adalah: Rp{kembalian}\n")
