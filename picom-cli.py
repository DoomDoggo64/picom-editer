import argparse
#made with ai im lazy :(
def edit_picom_conf(file_path, key, new_value=None, increment=None):
    # Read the existing configuration
    with open(file_path, 'r') as file:
        lines = file.readlines()

    # Flag to check if the key was found
    key_found = False

    # Modify the desired key
    for i, line in enumerate(lines):
        # Check if the line starts with the key
        if line.startswith(key):
            key_found = True
            # Extract the current value
            current_value_str = line.split('=')[1].strip()  # Get the value part
            current_value_list = list(current_value_str)
            
            
            # Try to convert the current value to a number
            count =0 
            while current_value_list[count] != '.':
                if current_value_list[count] == ';' :
                    count = 99 
                    break
                count +=1 
            else:
                if count ==99:
                    current_value = current_value_list[0]
                else:    
                    current_value = float("".join(current_value_list))

            # If increment is specified, increase the value
            if increment is not None:
                if 0 > (increment+current_value) or (increment+current_value) > 1:
                    print('Excedes 100 or is negative')
                    return
                else:
                    
                    new_value = current_value + increment 
                    
            # If a new value is specified, use that instead
            if new_value is not None:
                lines[i] = f"{key} = {new_value}\n"
            else:
                print(f"No new value or increment specified for '{key}'.")


    # If the key was not found, you can choose to add it
    if not key_found:
        if new_value is not None:
            print(f"Key '{key}' not found. Adding it with value {new_value}.")
            lines.append(f"{key} = {new_value}\n")
        elif increment is not None:
            print(f"Key '{key}' not found. Adding it with initial value {increment}.")
            lines.append(f"{key} = {increment}\n")

    # Write the modified configuration back to the file
    with open(file_path, 'w') as file:
        file.writelines(lines)


def main():   
    parser = argparse.ArgumentParser()
    parser.add_argument("-s","--set",type = int,help="sets opacity to the number entered")
    parser.add_argument("-a","--add",type= int,help="adds the number you put in to the current opacity")
    parser.add_argument("-b","--blur",action="store_true",help = "toggles blur on or off")

    args = parser.parse_args()

    if args.blur:
        return
    elif args.set is not None :
        print(args.set)
        if args.set not in range(0,101):
            print('Not a valid number to set the opacity to')
            return
        value = args.set / 100
        edit_picom_conf('picom.conf','inactive-opacity',new_value= value)
    elif args.add != None:
        value = args.add / 100
        edit_picom_conf('picom.conf','inactive-opacity', increment= value)

if __name__ == "__main__":
    main()