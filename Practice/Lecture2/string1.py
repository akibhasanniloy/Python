str1 = "This is a string.\nwe are creating it in python"
print(str1);

# Concatination
str2 = "Hello"
str3 = " World"
finalstr = str2+str3;
print(finalstr);

# Length
print(len(str2));

# indexing
str4 = "Hello World"
print(str4[0]);

# slicing
print(str4[1: 5]);
print(str4[6: len(str4)]);
print(str4[: 8]); #[0: 8]
print(str4[4:]); #[4: len(str4)]

str5 = "Apple";
print(str5[-4: -1]); #Backward counting

# String Function
str = "i am a coder.";
print(str.endswith("er."));
print(str.capitalize());
print(str.replace("coder", "Doctor"));
print(str.find("a"));
print(str.count("am"));

# practice problem 1
name = "Enter your first name: "
name1 = input(name);
print(len(name1));

# Practice 2
prb = "string"
print(prb.count("s"));