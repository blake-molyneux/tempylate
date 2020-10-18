import namepkg

#namepkg.main()

name = namepkg.Name(theme='', number=10)
name.gen_new_name()
print(name.output)
