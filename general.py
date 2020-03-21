import os


# Create folder location
def create_dir(directory):
    if not os.path.exists(directory):
        print('Creating directory: ' + directory)
        os.makedirs(directory)


# Create queue list files and crawled list files for saving progress
def create_files(site_name, base_url):
    queue = site_name + '/queue.txt'
    crawled = site_name + '/crawled.txt'
    if not os.path.isfile(queue):
        add_file(queue, base_url)
    if not os.path.isfile(crawled):
        add_file(crawled, '')


# Create a new file
def add_file(path, data):
    fw = open(path, 'w')
    fw.write(data)
    fw.close()


# Add to file
def add_to_file(path, data):
    with open(path, 'a') as file:
        file.write(data + '\n')
        

# Delete the contents of a file
def delete_file_contents(path):
    with open(path, 'w'):
        pass


# Read file and convert to set ("SPEEDUP", found on tutorial in Youtube)
def file_to_set(file_name):
    results = set()
    with open(file_name, 'rt') as fr:
        for line in fr:
            results.add(line.replace('\n', ''))
    return results


# Each item is a new line in file
def set_to_file(links, file):
    delete_file_contents(file)
    for link in sorted(links):
        add_to_file(file, link)
