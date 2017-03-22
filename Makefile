wikis = $(shell for F in tutorials/*.md; do echo .dokuwiki/$${F%.md}.txt; done)
deploys = $(shell for F in tutorials/*.md; do echo phony/deploys/$${F%.md}; done)
pdfs = $(shell for F in tutorials/*.md; do echo phony/pdfs/$${F%.md}; done)

convert: $(wikis)

deploy: $(deploys) deploy_pdfs

convert_pdfs: $(pdfs)

deploy_pdfs: convert_pdfs bin/post-image
	for pdf in .pdfs/tutorials/*.pdf; do bin/post-image "$$pdf"; done

.dokuwiki/tutorials:
	mkdir -p "$@"

.pdfs/tutorials:
	mkdir -p "$@"

.dokuwiki/tutorials/%.txt: tutorials/%.md bin/convert | .dokuwiki/tutorials .pdfs/tutorials
	bin/convert "$<"

phony/deploys/tutorials/%: .dokuwiki/tutorials/%.txt
	bin/deploy "$<"
	while read img; do bin/post-image tutorials/"$$img"; done < "$<".images

phony/pdfs/tutorials/%: .dokuwiki/tutorials/%.txt
	while read link; do bin/link-to-pdf "$$link"; done < "$<".links

clean:
	rm .dokuwiki .pdfs -rf || :

.PHONY: clean convert deploy convert_pdfs deploy_pdfs

# deploys are also phony, but that would not work with % target
