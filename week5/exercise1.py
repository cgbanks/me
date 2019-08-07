# -*- coding: UTF-8 -*-
"""Refactoring.

This exercise contains a complete and working example, but it's very poorly written.

Your job is to go through it and make it as good as you can.

That means making it self-documenting wherever possible, adding comments where
it isn't. Take repeated code and make it into a function. Also use functions
to encapsulate concepts. If something is done many times, maybe a map or a loop
is called for. Etc.

Some functions will have directions as external comments, once you think you
are on top of it, take these comments out. Others won't have comments and
you'll need to figure out for yourself what to do.
"""


# return a list of countdown messages, much like in the bad function above.
# It should say something different in the last message.
def countdown(message, start, stop, completion_message):
    countlist = []
    for i in range(int((start-stop)+1),0, -1):
        print(str(message) + " " + str(i))
    print(completion_message)
    return countlist


# TRIANGLES

# This should be a series of functions that are ultimatly used by
# triangle_master
# It should eventually return a dictionary of triangle facts. It should
# optionally print information as a nicely formatted string. Make printing
# turned off by default but turned on with an optional argument.
# The stub functions are made for you, and each one is tested, so this should
# hand hold quite nicely.
def calculate_hypotenuse(base, height):
    hypotenuse = ((base**2 + height**2)**(1/2))
    return(hypotenuse)


def calculate_area(base, height):
    area = ((height*base)/2)
    return(area)

def calculate_perimeter(base, height):
    perimeter = (base*base + height*height)**(1/2) + height + base
    return(perimeter)


def calculate_aspect(base, height):
    aspect = ""
    if height > base:
        aspect = "tall"
    elif base > height:
        aspect = "wide"
    else:
        aspect = "equal"
    return aspect


# Make sure you reuse the functions you've already got
# Don't reinvent the wheel
def get_triangle_facts(base, height, units="mm"):
    return {
        "area": calculate_area(base, height),
        "perimeter": calculate_perimeter(base, height),
        "height": height,
        "base": base,
        "hypotenuse": calculate_hypotenuse(base, height),
        "aspect": calculate_aspect(base, height),
        "units": units,
    }


# this should return a multi line string that looks a bit like this:
#
# 15
# |
# |     |\
# |____>| \  17.0
#       |  \
#       |   \
#       ------
#       8
# This triangle is 60.0mm²
# It has a perimeter of 40.0mm
# This is a tall triangle.
#
# but with the values and shape that relate to the specific
# triangle we care about.
def tell_me_about_this_right_triangle(facts_dictionary):
    tall = """
            {height}
            |
            |     |\\
            |____>| \\  {hypotenuse}
                  |  \\
                  |   \\
                  ------
                  {base}"""
    wide = """
            {hypotenuse}
             ↓         ∕ |
                   ∕     | <-{height}
               ∕         |
            ∕------------|
              {base}"""
    equal = """
            {height}
            |
            |     |⋱
            |____>|  ⋱ <-{hypotenuse}
                  |____⋱
                  {base}"""

    pattern = (
        "This triangle is {area}{units}²\n"
        "It has a perimeter of {perimeter}{units}\n"
        "This is a {aspect} triangle.\n"
    )

    area = calculate_area
    perimeter = calculate_perimeter
    aspect = calculate_aspect
    if facts_dictionary["aspect"] == "tall":
        diagram = tall.format(**facts_dictionary)
    elif facts_dictionary["aspect"] == "wide":
        diagram = wide.format(**facts_dictionary)
    else:
        diagram = equal.format(**facts_dictionary)
    facts = pattern.format(**facts_dictionary)
    return( diagram + "\n" + facts)

def triangle_master(base, height, return_diagram=False, return_dictionary=False):
    fax=get_triangle_facts(base, height)
    rightangle=tell_me_about_this_right_triangle(fax)
    if return_diagram and return_dictionary:
        return {"diagram": rightangle, "facts":fax}
    elif return_diagram:
        return rightangle
    elif return_dictionary:
        return fax
    else:
        print("You're an odd one, you don't want anything!")

def wordy_pyramid(api_key):
    import requests

    
    urllink = "https://us-central1-waldenpondpress.cloudfunctions.net/give_me_a_word?wordlength={len}"
    minword = 3
    maxword = 20
    wordlist = []
    firstlist =[]
    secondlist =[]
    for i in range(minword,maxword+1):
        newurl=urllink.format(len=i)
        pull = requests.get(newurl)   
        if pull.status_code is 200:         
            randomword = pull.content  
            if randomword is None: 
                pass
            else:
                randomword = str(randomword)
                if int(i) % 2 ==0:
                    secondlist.append(randomword[2:len(randomword)-1])    
                else:
                    firstlist.append(randomword[2:len(randomword)-1])
    secondlist.reverse()
    wordlist.extend(firstlist)
    wordlist.extend(secondlist)
    return wordlist  



def get_a_word_of_length_n(length):
    import requests
    baseURL = "https://us-central1-waldenpondpress.cloudfunctions.net/give_me_a_word?wordlength={lengthy}"
    if type(length) == int and length >=3:
        actualurl = baseURL.format(lengthy=length)
        r = requests.get(actualurl)
        if r.status_code is 200:
            grabbedword = str(r.content)
            returning = grabbedword[2:len(grabbedword)-1]
        return returning
    else:
        return None

def list_of_words_with_lengths(list_of_lengths):
    import requests
    listlength = []
    baseURL = "https://us-central1-waldenpondpress.cloudfunctions.net/give_me_a_word?wordlength={lengthy}"
    for j in list_of_lengths:
        url = baseURL.format(lengthy=j)
        r = requests.get(url)
        if r.status_code is 200:
            gottedword = str(r.content)
            returning = gottedword[2:len(gottedword)-1]
        listlength.append(returning)
    return listlength


if __name__ == "__main__":
    #do_bunch_of_bad_things()
    wordy_pyramid("a2a73e7b926c924fad7001ca3111acd55af2ffabf50eb4ae5")
