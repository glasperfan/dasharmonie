SOURCES = \
Test.ml \
Test2.ml

all: $(SOURCES)
	corebuild -quiet -lib graphics Main.native

clean:
	rm -rf _build *.native