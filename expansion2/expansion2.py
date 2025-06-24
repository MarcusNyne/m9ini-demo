from m9ini import uConfig

# Enable print failures to console
uConfig.PrintFailures()

# Load configuration
config = uConfig("expansion2.ini")

# Print demo settings
demo_section = config.GetSection("Demo")
print (demo_section.FormatString(">>> [=Id] [=Name]"))
print ('-' * 66)
for line in config.GetSection("Description").GetTextBlock():
    print(line)

# Perform test
print ('-' * 66)
print (f'There are {config.CountSections("Test")} Test sections.')

print ('')
print ('Printing Test section combinations:')
test_sections = config.GetSectionsBySpec("Test")
for section in test_sections:
    print (section.FormatString(" - [=*id]: [=Description]"))

# Write output file
print ('-' * 66)
out_filename = demo_section.GetValue("OutputFile")
print (f"Writing output file: {out_filename}")
config.WriteConfigLines(out_filename)
