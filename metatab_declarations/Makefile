

.PHONY: upload

sources := $(shell ls *.csv)
destfiles := $(patsubst %.csv,%.json,$(sources))

all: $(destfiles)

%.json: %.csv
	metatab -d -j $*.csv > $*.json
	aws s3 cp  $*.csv s3://assets.metatab.org/ --acl public-read
	aws s3 cp  $*.json s3://assets.metatab.org/ --acl public-read


clean:
	rm *.json