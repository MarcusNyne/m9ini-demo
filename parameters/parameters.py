from m9ini import uConfig

# Enable print failures to console
uConfig.PrintFailures()

# Load configuration
config = uConfig("parameters.ini", ['animal=cat', 'Test.shape=triangle'])

# Print demo settings
demo_section = config.GetSection("Demo")
print (demo_section.FormatString(">>> [=Id] [=Name]"))
print ('-' * 66)
for line in config.GetSection("Description").GetTextBlock():
    print(line)

# Perform test
print ('-' * 66)
test_section = config.GetSection("Test")
print("Root animal is "+str(config.GetValue("animal")))
print("Test animal is "+str(test_section.GetValue("animal")))
print("Root shape is "+str(config.GetValue("shape")))
print("Test shape is "+str(test_section.GetValue("shape")))
print(test_section.FormatString("Description is [=Description]"))

# Write output file
print ('-' * 66)
out_filename = demo_section.GetValue("OutputFile")
print (f"Writing output file: {out_filename}")
config.WriteConfigLines(out_filename)
