import csv
import os
import yaml

# Specify the file path for Fields Summary input.
csv_map_summary = "botes-csv-summary/BOTES-Fields-Summary.csv"

# Specify the output directory for BOTES ECS Fieldset schema.
botes_schema_folder = "schemas-botes/"

# Specify the output directory for BOTES Logstash configuration.
logstash_conf_folder = "botes-logstash-conf/"

# Specify the folder path for mapping CSV files.
csv_map_files = "botes-csv-map/"

# The following list contains all existing ECS fieldsets.
existing_fieldsets = ["base", "agent", "as", "client", "cloud", "container", "destination", "dns", "ecs", "error",
                      "event", "file", "geo", "group", "hash", "host", "http", "log", "message", "network", "observer",
                      "organization", "os", "process", "related", "server", "service", "source", "trace", "transaction",
                      "url", "user", "user_agent"]

# To avoid conflict with future release of ECS, all new fields in existing
# fieldsets are added in a custom fieldset called "BOTES".
# New fieldsets will be also created for new fields.
# The following list will contain all new detected fieldsets from the CSV summary.
new_fieldsets = []

# Because some fields appear multiple time in Summary Field file, they will be added to the following table to avoid
# to create them multiple time in YAML Schema files. Define group variable for Schema heading.
new_fields = []

# Define Group variable for Schema heading.
group = 2

# Define Short Description variable for Schema heading.
short_desc = "Please insert new ECS fieldset short description here"

# Define Long Description variable for Schema heading.
long_desc = "Please insert new ECS fieldset long description here"


def new_fieldset_header(fieldset_name, fieldset_group, fieldset_short_desc,
                        fieldset_long_desc, fieldset_type):
    header = {"name": fieldset_name, "title": fieldset_name.title(), "group": fieldset_group,
              "short": fieldset_short_desc, "description": fieldset_long_desc, "type": fieldset_type}
    return header


def new_field(field_name, field_level, field_type, field_desc):
    field = {"name": field_name, "level": field_level.lower(), "type": field_type.lower(), "description": field_desc}
    return field


def dump_yaml(header, fields_list, yaml_filename):
    if not os.path.exists(botes_schema_folder):
    	os.makedirs(botes_schema_folder)
    field_yaml = {"fields": fields_list}
    schema_yaml = [{**header, **field_yaml}]
    with open(botes_schema_folder + yaml_filename + ".yml", 'w') as new_schema_file:
        new_schema_file.write("---\n")
        yaml.dump(schema_yaml, new_schema_file, default_flow_style=False, sort_keys=False)


def create_schemas_file():
    with open(csv_map_summary, 'r') as file_in:
        fields_summary = csv.reader(file_in)
        # Skip CSV header
        next(fields_summary)
        for row_list in fields_summary:
            ecs_field = row_list[1]
            ecs_fieldset = ecs_field.split('.')[0]
            # New fieldset fields will be added to the following list, to be dump in YAML file.
            # List will be emptied between each different new fieldset found.
            fieldset_field_list = []
            if ecs_fieldset not in existing_fieldsets and ecs_fieldset not in new_fieldsets:
                # Add fieldset to the new fieldset list.
                new_fieldsets.append(ecs_fieldset)
                # Create dict containing new fieldset schema heading elements.
                fieldset_header = new_fieldset_header(ecs_fieldset, 2, short_desc, long_desc, "group")
                with open(csv_map_summary, 'r') as sfile:
                    sfields = csv.reader(sfile)
                    next(sfields)
                    for rows in sfields:
                        search_fields = rows[1]
                        fname = rows[1].replace(search_fields.split('.')[0]+'.', '')
                        ftype = rows[2]
                        flevel = rows[4]
                        fdesc = rows[5]
                        if search_fields.split('.')[0] == ecs_fieldset and search_fields not in new_fields:
                            new_fields.append(search_fields)
                            fieldset_field = new_field(fname, flevel, ftype, fdesc)
                            fieldset_field_list.append(fieldset_field)
                dump_yaml(fieldset_header, fieldset_field_list, ecs_fieldset)


def create_logstash_mutate():
    if not os.path.exists(logstash_conf_folder):
        os.makedirs(logstash_conf_folder)
    for mapping_files in os.listdir(csv_map_files):
        fm = open(logstash_conf_folder + mapping_files.split('.')[0] + ".conf", 'w')
        fm.write("filter {\n\tmutate {\n")
        with open(csv_map_files + mapping_files, 'r') as map_files:
            field_mapping = csv.reader(map_files)
            # Skip CSV header
            next(field_mapping)
            for row_field_mapping in field_mapping:
                original_field = row_field_mapping[0]
                ecs_field = row_field_mapping[1]

                fm.write("\t\trename => [\"" + original_field + "\", \"" + ecs_field + "\"]\n")
        fm.write("\t}\n}")


def call_ecs_generator():
	os.system("python scripts/generator.py --include " + botes_schema_folder)


def main():
    print("Creating ECS Schema files for new fieldset...")
    create_schemas_file()
    print("Schema files for the following new fieldsets have been created:")
    print(*new_fieldsets, sep=' | ')
    print("Done.")
    print("\nCreating Logstash mutate configuration for ECS normalization...")
    create_logstash_mutate()
    print("Done.")
    print("\nCalling ECS generator script for Elastisearch Mapping and docs files creation...")
    call_ecs_generator()
    print("Done.")

if __name__ == "__main__":
    main()
