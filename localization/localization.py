from m9ini import uConfig

# Enable print failures to console
uConfig.PrintFailures()

# Load configuration
config = uConfig("localization.ini")

# Print demo settings
demo_section = config.GetSection("Demo")
print (demo_section.FormatString(">>> [=Id] [=Name]"))
print ('-' * 66)
for line in config.GetSection("Description").GetTextBlock():
    print(line)

# List test parameters
print ('-' * 66)
print (demo_section.FormatString("Language is set to [=Language]"))
print ('CurrentLanguage is '+config.GetSectionValue("Test", "CurrentLanguage"))
print ('LanguageSection is '+str(config.GetSectionValue("Test", "LanguageSection")))

# Perform test
print ('-' * 66)
language = config.GetSectionLink("Test", "LanguageSection")
print (language.FormatString("[=Hello]"))
print (language.FormatString("[=*id] is good for [=Goodfor]"))
print ("Favorite bird is " + config.GetSectionValue("Test", "FavoriteBird"))
print ("Favorite flower is " + config.GetSectionValue("Test", "FavoriteFlower"))

# Write output file
print ('-' * 66)
out_filename = demo_section.GetValue("OutputFile")
print (f"Writing output file: {out_filename}")
config.WriteConfigLines(out_filename)
