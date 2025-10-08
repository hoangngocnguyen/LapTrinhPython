from pathlib import Path

print(Path('usr').joinpath('bin').joinpath('spam1'))

# hoặc Path('usr') / 'bin' / 'spam1'

my_files = ['accounts.txt', 'details.csv', 'invite.docx']
home = Path.home()      # Lấy đường dẫn home (user)
for filename in my_files:
    print(home / filename)

cwd = Path.cwd()
print(cwd)

(cwd / "hello" / "son").mkdir(parents=True)


print(cwd.is_absolute())

