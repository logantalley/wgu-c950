from datetime import datetime

class HashBrowns(object):
    def __init__(self, length=40):
        if isinstance(length, int):
            if length >= 1:
                self.dictionary = length * [None]
            else:
                raise ValueError("Size can't be 0 or negative!")
        else:
            raise ValueError("Hash table size should be an integer")
    
    def __len__(self):
        return len(self.dictionary)
    
    def keys(self):
        return set([key_pair[0] for key_pair in self.dictionary if key_pair])
    def values(self):
        return [key_pair[1] for key_pair in self.dictionary if key_pair]
    
    def get(self, key_str):
        index = self.get_index(key_str)
        if self.dictionary[index]:
            return self.dictionary[index][1]

    def get_index(self, key):
        return int(key.split('_')[1]) - 1
    def append(self, key, value):
        index = self.get_index(key)
        self.dictionary[index] = (key, value)
                
    def __setitem__(self, key, value):
        self.append(key, value)
    
    def __getitem__(self, key_str):
        return self.get(key_str)
    
    def __iter__(self):
        yield from self.keys()

    def print_em(self, print_type):
        if print_type == 'all':
            print('{\n')
            for key_pair in self.dictionary:
                print(f"{key_pair[0]}:{key_pair[1]},\n")
            print('}')
    def __main__(self):
        self.print_em('all')
    def items(self):
        self.print_em('all')

    def lookup(self, element, query):
        return [key_pair[1].all for key_pair in self.dictionary if query == str(getattr(key_pair[1], element))]
    
        
    
class TaterTot:
    def __init__(self, pkg_id, address, deadline, city, zip_code, mass, special_notes, status):
        if isinstance(pkg_id, int):
            self.pkg_id = pkg_id
        else:
            raise ValueError("pkg_id must be int!")
        
        if isinstance(address, str):
            self.address = address
        else:
            raise ValueError("address must be str!")
        
        if isinstance(deadline, str):
            if deadline != 'EOD':
                try:
                    self.deadline = datetime.strptime(deadline, '%I:%M %p')
                except:
                    raise ValueError("deadline must be in %I:%M %p format!") 
            else:
                self.deadline = deadline
        else:
            raise ValueError("deadline must be in %H:%M format or EOD!")
        
        if isinstance(city, str):
            self.city = city
        else:
            raise ValueError("city must be str!")
        
        if isinstance(zip_code, int):
            self.zip_code = zip_code
        else:
            raise ValueError("zip_code must be int!")
        
        if isinstance(mass, float):
            self.mass = mass
        else:
            raise ValueError("mass must be float!")
        
        if isinstance(special_notes, str) or special_notes == None:
            self.special_notes = special_notes
        else:
            raise ValueError("special_notes must be str!")
        
        if isinstance(status, str):
            self.status = status
        else:
            raise ValueError("status must be str!")

    @property
    def all(self):
        all_dict = {
            'pkg_id': self.pkg_id,
            'address': self.address,
            'deadline': self.deadline,
            'city': self.city,
            'zip_code': self.zip_code,
            'mass': self.mass,
            'special_notes': self.special_notes,
            'status': self.status
        }
        return all_dict

