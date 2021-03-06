"""Functions to parse a file containing student data."""


def all_houses(filename):
    """Return a set of all house names in the given file.

    For example:
      >>> unique_houses('cohort_data.txt')
      {"Dumbledore's Army", 'Gryffindor', ..., 'Slytherin'}

    Arguments:
      - filename (str): the path to a data file

    Return:
      - set[str]: a set of strings
    """
    data = open(filename)

    houses = []

    # TODO: replace this with your code
    for line in data:
      line.rstrip()
      list = line.split('|')

      house = list[2]

      if house != '':
        houses.append(house)



    data.close()

    return set(houses)


def students_by_cohort(filename, cohort='All'):
    """Return a list of students' full names by cohort.

    Names are sorted in alphabetical order. If a cohort isn't
    given, return a list of all students. For example:
      >>> students_by_cohort('cohort_data.txt')
      ['Adrian Pucey', 'Alicia Spinnet', ..., 'Zacharias Smith']

      >>> students_by_cohort('cohort_data.txt', cohort='Fall 2015')
      ['Angelina Johnson', 'Cho Chang', ..., 'Terence Higgs', 'Theodore Nott']

      >>> students_by_cohort('cohort_data.txt', cohort='Winter 2016')
      ['Adrian Pucey', 'Andrew Kirke', ..., 'Roger Davies', 'Susan Bones']

      >>> students_by_cohort('cohort_data.txt', cohort='Spring 2016')
      ['Cormac McLaggen', 'Demelza Robins', ..., 'Zacharias Smith']

      >>> students_by_cohort('cohort_data.txt', cohort='Summer 2016')
      ['Alicia Spinnet', 'Dean Thomas', ..., 'Terry Boot', 'Vincent Crabbe']

    Arguments:
      - filename (str): the path to a data file
      - cohort (str): optional, the name of a cohort

    Return:
      - list[list]: a list of lists
    """
    file = open(filename)

    students = []

    # TODO: replace this with your code

    for line in file:
      line = line.rstrip('\r\n')
      data = line.split('|')
      # print(f'Data: {data[4]}')
      # print(f'Cohort: {cohort}')
      if cohort == data[4]:
        first_name = data[0]
        last_name = data[1]
        full_name = first_name + ' ' + last_name

        students.append(full_name)
      elif cohort == 'All' and data[4] != 'G' and data[4] != 'I':

        first_name = data[0]
        last_name = data[1]
        full_name = first_name + ' ' + last_name

        students.append(full_name)

    file.close()

    return sorted(students)


def all_names_by_house(filename):
    """Return a list that contains rosters for all houses, ghosts, instructors.

    Rosters appear in this order:
    - Dumbledore's Army
    - Gryffindor
    - Hufflepuff
    - Ravenclaw
    - Slytherin
    - Ghosts
    - Instructors

    Each roster is a list of names sorted in alphabetical order.

    For example:
      >>> rosters = hogwarts_by_house('cohort_data.txt')
      >>> len(rosters)
      7

      >>> rosters[0]
      ['Alicia Spinnet', ..., 'Theodore Nott']
      >>> rosters[-1]
      ['Filius Flitwick', ..., 'Severus Snape']

    Arguments:
      - filename (str): the path to a data file

    Return:
      - list[list]: a list of lists
    """

    dumbledores_army = []
    gryffindor = []
    hufflepuff = []
    ravenclaw = []
    slytherin = []
    ghosts = []
    instructors = []

    # TODO: replace this with your code

    file = open(filename)

    names_by_house = []

    for line in file:
      line = line.rstrip('\r\n')
      data = line.split('|')

      # print(data)

      #if data[-1] == 'G', goes into ghosts list
      if data[-1] == 'G':
        first_name = data[0]
        last_name = data[1]
        full_name = first_name + ' ' + last_name

        ghosts.append(full_name)

      #if data [-1] == 'I', goes into instructors list
      elif data[-1] == 'I':
        first_name = data[0]
        last_name = data[1]
        full_name = first_name + ' ' + last_name

        instructors.append(full_name)

      #else if data[2] == 'Gryffindor', goes in gry
      elif data[2] == 'Gryffindor':
        first_name = data[0]
        last_name = data[1]
        full_name = first_name + ' ' + last_name

        gryffindor.append(full_name)

      elif data[2] == "Hufflepuff":
        first_name = data[0]
        last_name = data[1]
        full_name = first_name + ' ' + last_name

        hufflepuff.append(full_name)

      elif data[2] == "Dumbledore's Army":
        first_name = data[0]
        last_name = data[1]
        full_name = first_name + ' ' + last_name

        dumbledores_army.append(full_name)

      elif data[2] == "Ravenclaw":
        first_name = data[0]
        last_name = data[1]
        full_name = first_name + ' ' + last_name

        ravenclaw.append(full_name)

      elif data[2] == "Slytherin":
        first_name = data[0]
        last_name = data[1]
        full_name = first_name + ' ' + last_name

        slytherin.append(full_name)


      # first_name = data[0]
      #   last_name = data[1]
      #   full_name = first_name + ' ' + last_name


    file.close()

    return [sorted(dumbledores_army), sorted(gryffindor), sorted(hufflepuff), sorted(ravenclaw), sorted(slytherin), sorted(ghosts), sorted(instructors)]


def all_data(filename):
    """Return all the data in a file.

    Each line in the file is a tuple of (full_name, house, advisor, cohort)

    Iterate over the data to create a big list of tuples that individually
    hold all the data for each person. (full_name, house, advisor, cohort)

    For example:
      >>> all_student_data('cohort_data.txt')
      [('Harry Potter', 'Gryffindor', 'McGonagall', 'Fall 2015'), ..., ]

    Arguments:
      - filename (str): the path to a data file

    Return:
      - list[tuple]: a list of tuples
    """

    file = open(filename)

    all_data = []

    for line in file:
      line = line.rstrip('\r\n')
      data = line.split('|')
      full_name = data[0] + ' ' + data[1]

      data[0] = full_name
      data.pop(1)
      # print(data)
      
      data = tuple(data)
      all_data.append(data)

    # TODO: replace this with your code

    file.close()

    return all_data


def get_cohort_for(filename, name):
    """Given someone's name, return the cohort they belong to.

    Return None if the person doesn't exist. For example:
      >>> get_cohort_for('cohort_data.txt', 'Harry Potter')
      'Fall 2015'

      >>> get_cohort_for('cohort_data.txt', 'Hannah Abbott')
      'Winter 2016'

      >>> get_cohort_for('cohort_data.txt', 'Balloonicorn')
      None

    Arguments:
      - filename (str): the path to a data file
      - name (str): a person's full name

    Return:
      - str: the person's cohort or None
    """

    # TODO: replace this with your code
    file = open(filename)

    for line in file:
      line = line.rstrip('\r\n')
      data = line.split('|')

      full_name = data[0] + ' ' + data[1]

      if name != full_name:
        None
      elif name == full_name:
        cohort = data[-1]
        return cohort

    file.close()


def find_duped_last_names(filename):
    """Return a set of duplicated last names that exist in the data.

    For example:
      >>> find_name_duplicates('cohort_data.txt')
      {'Creevey', 'Weasley', 'Patil'}

    Arguments:
      - filename (str): the path to a data file

    Return:
      - set[str]: a set of strings
    """

    # TODO: replace this with your code
    file = open(filename)

    duplicates = set()
    last_names = set()

    for line in file:
      line = line.rstrip('\r\n')
      data = line.split('|')

      last_name = data[1]

      if last_name in last_names:
        duplicates.add(last_name)

      last_names.add(last_name)


    file.close()

    return duplicates


def get_housemates_for(filename, name):
    """Return a set of housemates for the given student.

    Given a student's name, return a list of their housemates. Housemates are
    students who belong to the same house and were in the same cohort as the
    given student.

    For example:
    >>> get_housemates_for('cohort_data.txt', 'Hermione Granger')
    {'Angelina Johnson', ..., 'Seamus Finnigan'}
    """

    # TODO: replace this with your code


##############################################################################
# END OF MAIN EXERCISE.  Yay!  You did it! You Rock!
#

if __name__ == '__main__':
    import doctest

    result = doctest.testfile('doctests.py',
                              report=False,
                              optionflags=(
                                  doctest.REPORT_ONLY_FIRST_FAILURE
                              ))
    doctest.master.summarize(1)
    if result.failed == 0:
        print('ALL TESTS PASSED')
