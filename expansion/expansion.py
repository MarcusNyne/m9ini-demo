from m9ini import uConfig

# Enable print failures to console
uConfig.PrintFailures()

# Load configuration
config = uConfig("expansion.ini")

# Print demo settings
demo_section = config.GetSection("Demo")
print (demo_section.FormatString(">>> [=Id] [=Name]"))
print ('-' * 66)
for line in config.GetSection("Description").GetTextBlock():
    print(line)

# Perform test
print ('-' * 66)
print (f'There are {config.CountSections(":colors")} Test:colors sections.')
print (f'There are {config.CountSections(":list")} Test:list sections.')
print (f'There are {config.CountSections(":block")} Test:block sections.')
print (f'There are {config.CountSections(":numbers")} Test:numbers sections.')

print ('')
print ('Printing Test:list section descriptions:')
test_sections = config.GetSectionsBySpec(":list")
for section in test_sections:
    print (section.FormatString(" - [=Description]"))

print ('')
print ('Printing Test:numbers section combinations:')
test_sections = config.GetSectionsBySpec(":numbers")
for section in test_sections:
    print (section.FormatString(" - [=Value1], [=Value2]"))

# Write output file
print ('-' * 66)
out_filename = demo_section.GetValue("OutputFile")
print (f"Writing output file: {out_filename}")
config.WriteConfigLines(out_filename)
