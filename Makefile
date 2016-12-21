wikis = $(shell for F in tutorials/*.md; do echo .dokuwiki/$${F%.md}.txt; done)
deploys = $(shell for F in tutorials/*.md; do echo phony/$${F%.md}; done)

convert: $(wikis)

deploy: $(deploys)

.dokuwiki/tutorials:
	mkdir -p "$@"

.dokuwiki/tutorials/%.txt: tutorials/%.md bin/convert | .dokuwiki/tutorials
	bin/convert "$<"

phony/tutorials/%: .dokuwiki/tutorials/%.txt
	bin/deploy "$<"

clean:
	rm .dokuwiki -rf || :

.PHONY: clean convert deploy

# deploys are also phony, but that would not work with % target
