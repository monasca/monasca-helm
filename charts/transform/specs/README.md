# Monasca-transform specs

Monasca transform aggregates metrics based on the pre-transform and transform specs stored in the database.

NCS requirements of aggregation differ from those of the upstream openstack repo so generating and maintaining our own database population scripts is essential.
 
####Generating sql

Our maintained json specs files are here.  To generate sql for the database the scripts/generate_ddl.sh script in the monascat-transform repo may be used and the generated sql file copied here alongside the source json files.