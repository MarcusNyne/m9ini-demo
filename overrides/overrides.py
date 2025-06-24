from m9ini import uConfig

# Enable print failures to console
uConfig.PrintFailures()

# Load configuration
config = uConfig("overrides.ini")

# Print demo settings
demo_section = config.GetSection("Demo")
print (demo_section.FormatString(">>> [=Id] [=Name]"))
print ('-' * 66)
for line in config.GetSection("Description").GetTextBlock():
    print(line)

# Perform test
print ('-' * 66)
test_section = config.GetSection("Test")
print("Test:one ColorList is "+str(config.GetSectionValue(":one", "ColorList")))
print("Test:two ColorList is "+str(config.GetSectionValue(":two", "ColorList")))

# Write output file
print ('-' * 66)
out_filename = demo_section.GetValue("OutputFile")
print (f"Writing output file: {out_filename}")
config.WriteConfigLines(out_filename)
