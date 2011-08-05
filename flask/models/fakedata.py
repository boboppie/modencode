#!/usr/bin/python
# -*- coding: utf -*-

# TODO: remove this when done

data = {
"categories" : [ { "category" : "Chromatin structure",
        "organisms" : [ { "experiments" : [ { "experiment_title" : "Genome-wide Chromatin Profiling",
                    "labs" : [ "Kamran Ahmad",
                        "Steven Henikoff"
                      ],
                    "pi" : "Steven Henikoff"
                  } ],
              "organism" : "D. melanogaster"
            },
            { "experiments" : [ { "experiment_title" : "Nucleosome mapping",
                    "labs" : [ "Jason Lieb" ],
                    "pi" : "Jason Lieb"
                  },
                  { "experiment_title" : "Genome wide chromatin profiling in C. elegans",
                    "labs" : [ "Steven Henikoff" ],
                    "pi" : "Steven Henikoff"
                  }
                ],
              "organism" : "C. elegans"
            }
          ]
      },
      { "category" : "Copy Number Variation",
        "organisms" : [ { "experiments" : [ { "experiment_title" : "CGH drosophila cell lines",
                    "labs" : [ "David MacAlpine" ],
                    "pi" : "David MacAlpine"
                  },
                  { "experiment_title" : "CNV in Drosophila cell lines",
                    "labs" : [ "David MacAlpine" ],
                    "pi" : "David MacAlpine"
                  },
                  { "experiment_title" : "Differential Replication of Polytene Chromosomes",
                    "labs" : [ "Terry Orr-Weaver" ],
                    "pi" : "David MacAlpine"
                  }
                ],
              "organism" : "D. melanogaster"
            },
            { "experiments" : [  ],
              "organism" : "C. elegans"
            }
          ]
      },
      { "category" : "Gene Structure",
        "organisms" : [ { "experiments" : [ { "experiment_title" : "RT-PCR",
                    "labs" : [ "Michael Brent" ],
                    "pi" : "Sue Celniker"
                  },
                  { "experiment_title" : "Analysis of TSS using stranded RACE products",
                    "labs" : [ "Sue Celniker" ],
                    "pi" : "Sue Celniker"
                  },
                  { "experiment_title" : "5' RACE",
                    "labs" : [ "Sue Celniker" ],
                    "pi" : "Sue Celniker"
                  },
                  { "experiment_title" : "Confirmation of Drosophila transcripts by full-length cDNA screening",
                    "labs" : [ "Sue Celniker" ],
                    "pi" : "Sue Celniker"
                  },
                  { "experiment_title" : "Annotation of Drosophila splice junctions by RNA-seq",
                    "labs" : [ "Brenton Graveley" ],
                    "pi" : "Sue Celniker"
                  },
                  { "experiment_title" : "Cap Analysis of Gene Expression",
                    "labs" : [ "Sue Celniker" ],
                    "pi" : "Sue Celniker"
                  },
                  { "experiment_title" : "Drosophila Cell Line and Developmental Stage Gene and Exon Scores",
                    "labs" : [ "Peter Cherbas" ],
                    "pi" : "Sue Celniker"
                  },
                  { "experiment_title" : "Gene Model Prediction",
                    "labs" : [ "Michael Brent" ],
                    "pi" : "Sue Celniker"
                  }
                ],
              "organism" : "D. melanogaster"
            },
            { "experiments" : [ { "experiment_title" : "Encyclopedia of C. elegans 3'UTRs and their regulatory elements",
                    "labs" : [ "Fabio Piano",
                        "John Kim"
                      ],
                    "pi" : "Fabio Piano"
                  },
                  { "experiment_title" : "SL Acceptor Site Confirmation in C. elegans",
                    "labs" : [ "Phil Green" ],
                    "pi" : "Robert Waterston"
                  },
                  { "experiment_title" : "Reanalysis of comprehensive set of C. elegans transcripts and expression for various stages and conditions",
                    "labs" : [ "Robert Waterston" ],
                    "pi" : "Robert Waterston"
                  },
                  { "experiment_title" : "Intron Confirmation in C. elegans",
                    "labs" : [ "Phil Green" ],
                    "pi" : "Robert Waterston"
                  },
                  { "experiment_title" : "Mass spectrometric validation of short ORFs",
                    "labs" : [ "Michael MacCoss" ],
                    "pi" : "Robert Waterston"
                  },
                  { "experiment_title" : "Identification of small RNAs in C. elegans",
                    "labs" : [ "Frank Slack" ],
                    "pi" : "Robert Waterston"
                  },
                  { "experiment_title" : "Transcription Start Site Confirmation in C. elegans",
                    "labs" : [ "Phil Green" ],
                    "pi" : "Robert Waterston"
                  }
                ],
              "organism" : "C. elegans"
            }
          ]
      },
      { "category" : "Histone modification and replacement",
        "organisms" : [ { "experiments" : [ { "experiment_title" : "HMM Prediction of D. melanogaster Chromatin States",
                    "labs" : [ "Gary Karpen" ],
                    "pi" : "Gary Karpen"
                  },
                  { "experiment_title" : "Genomic Distributions of Histone Modifications",
                    "labs" : [ "Gary Karpen",
                        "Mitzi Kuroda",
                        "Sarah Elgin",
                        "Vincent Pirrotta"
                      ],
                    "pi" : "Gary Karpen"
                  },
                  { "experiment_title" : "Chromatin Binding Site Mapping of Modified Histone Proteins in D. melanogaster",
                    "labs" : [ "Kevin White" ],
                    "pi" : "Kevin White"
                  }
                ],
              "organism" : "D. melanogaster"
            },
            { "experiments" : [ { "experiment_title" : "Chromatin ChIP-chip of Modified Histones in C. elegans",
                    "labs" : [ "Jason Lieb",
                        "Julie Ahringer",
                        "Susan Strome"
                      ],
                    "pi" : "Jason Lieb"
                  } ],
              "organism" : "C. elegans"
            }
          ]
      },
      { "category" : "Metadata only",
        "organisms" : [ { "experiments" : [ { "experiment_title" : "RNA made in Bloomington",
                    "labs" : [ "Peter Cherbas",
                        "Tom Gingeras"
                      ],
                    "pi" : "Sue Celniker"
                  } ],
              "organism" : "D. melanogaster"
            },
            { "experiments" : [  ],
              "organism" : "C. elegans"
            }
          ]
      },
      { "category" : "Other chromatin binding sites",
        "organisms" : [ { "experiments" : [ { "experiment_title" : "Genomic Distributions of non-Histone Chromosomal Proteins in D. melanogaster",
                    "labs" : [ "Gary Karpen",
                        "Mitzi Kuroda",
                        "Sarah Elgin",
                        "Vincent Pirrotta"
                      ],
                    "pi" : "Gary Karpen"
                  },
                  { "experiment_title" : "Chromatin Binding Site Mapping of non-Histone Chromosomal Proteins in D. melanogaster",
                    "labs" : [ "Kevin White" ],
                    "pi" : "Kevin White"
                  },
                  { "experiment_title" : "Classification of D. melanogaster Insulator Binding Sequences",
                    "labs" : [ "Kevin White" ],
                    "pi" : "Kevin White"
                  }
                ],
              "organism" : "D. melanogaster"
            },
            { "experiments" : [ { "experiment_title" : "Chromatin ChIP-chip",
                    "labs" : [ "Arshad Desai",
                        "Jason Lieb",
                        "Julie Ahringer",
                        "Susan Strome"
                      ],
                    "pi" : "Jason Lieb"
                  },
                  { "experiment_title" : "Chromatin ChIP-chip of non-Histone Chromosomal Proteins in C. elegans",
                    "labs" : [ "Jason Lieb" ],
                    "pi" : "Jason Lieb"
                  }
                ],
              "organism" : "C. elegans"
            }
          ]
      },
      { "category" : "RNA expression profiling",
        "organisms" : [ { "experiments" : [ { "experiment_title" : "Transcriptional Profiling of additional Drosophila species with RNA-Seq",
                    "labs" : [ "Brian Oliver" ],
                    "pi" : "Brian Oliver"
                  },
                  { "experiment_title" : "Transcriptional profiling of Drosophila cell lines",
                    "labs" : [ "Kamran Ahmad" ],
                    "pi" : "Steven Henikoff"
                  },
                  { "experiment_title" : "RNA-seq support of the ChIP data",
                    "labs" : [ "Kevin White" ],
                    "pi" : "Kevin White"
                  },
                  { "experiment_title" : "Small RNA identification",
                    "labs" : [ "Eric Lai",
                        "Gregory Hannon"
                      ],
                    "pi" : "Eric Lai"
                  },
                  { "experiment_title" : "Short read sequencing of fly mRNA",
                    "labs" : [ "Michael Brent" ],
                    "pi" : "Sue Celniker"
                  },
                  { "experiment_title" : "Transcriptional Profiling of D. melanogaster cell lines using Illumina poly(A)%2B RNA-Seq",
                    "labs" : [ "Brenton Graveley" ],
                    "pi" : "Sue Celniker"
                  },
                  { "experiment_title" : "Paired End RNA-Seq of Drosophila Cell Lines",
                    "labs" : [ "Brenton Graveley" ],
                    "pi" : "Sue Celniker"
                  },
                  { "experiment_title" : "Developmental Time Course Transcriptional Profiling of D. melanogaster Embryo Using SOLiD Stranded Total RNA-Seq",
                    "labs" : [ "Sue Celniker" ],
                    "pi" : "Sue Celniker"
                  },
                  { "experiment_title" : "Tissue-specific Transcriptional Profiling of D. melanogaster using Illumina poly(A)%2B RNA-Seq",
                    "labs" : [ "Brenton Graveley" ],
                    "pi" : "Sue Celniker"
                  },
                  { "experiment_title" : "Identification of transcribed sequences with expression profile maps",
                    "labs" : [ "Tom Gingeras" ],
                    "pi" : "Sue Celniker"
                  },
                  { "experiment_title" : "Stranded Cell Line Transcriptional Profiling Using Illumina poly%28A%29%2B RNA-seq",
                    "labs" : [ "Sue Celniker" ],
                    "pi" : "Sue Celniker"
                  },
                  { "experiment_title" : "Capped and uncapped short RNAs",
                    "labs" : [ "Tom Gingeras" ],
                    "pi" : "Sue Celniker"
                  },
                  { "experiment_title" : "C-tailed RNA-Seq of Drosophila Cell lines and stages",
                    "labs" : [ "Tom Gingeras" ],
                    "pi" : "Sue Celniker"
                  },
                  { "experiment_title" : "Developmental Stage Timecourse Transcriptional Profiling with RNA-Seq",
                    "labs" : [ "Brenton Graveley",
                        "Sue Celniker"
                      ],
                    "pi" : "Sue Celniker"
                  },
                  { "experiment_title" : "RNAi of RNA splicing factors in D. melanogaster",
                    "labs" : [ "Brenton Graveley" ],
                    "pi" : "Sue Celniker"
                  }
                ],
              "organism" : "D. melanogaster"
            },
            { "experiments" : [ { "experiment_title" : "Assaying RNA Expression in C. elegans",
                    "labs" : [ "Jason Lieb" ],
                    "pi" : "Jason Lieb"
                  },
                  { "experiment_title" : "Transcriptional profiling of C. elegans N2 embryos",
                    "labs" : [ "Kamran Ahmad" ],
                    "pi" : "Steven Henikoff"
                  },
                  { "experiment_title" : "Small RNA expression in C. elegans embryos",
                    "labs" : [ "Nikolaus Rajewsky" ],
                    "pi" : "Fabio Piano"
                  },
                  { "experiment_title" : "Identification of tissue and stage-specific transcribed sequences with expression profile maps",
                    "labs" : [ "David Miller",
                        "Valerie Reinke"
                      ],
                    "pi" : "Robert Waterston"
                  },
                  { "experiment_title" : "Definition of comprehensive set of C. elegans transcripts and expression for various stages and conditions",
                    "labs" : [ "Robert Waterston" ],
                    "pi" : "Robert Waterston"
                  },
                  { "experiment_title" : "Changes in expression of small RNAs under stress conditions in C. elegans",
                    "labs" : [ "Frank Slack" ],
                    "pi" : "Robert Waterston"
                  },
                  { "experiment_title" : "Identification of transcribed sequences under pathogenic bacterial growth conditions with expression profile maps",
                    "labs" : [ "Valerie Reinke" ],
                    "pi" : "Robert Waterston"
                  },
                  { "experiment_title" : "Changes in expression of small RNAs during aging in C. elegans",
                    "labs" : [ "Frank Slack" ],
                    "pi" : "Robert Waterston"
                  }
                ],
              "organism" : "C. elegans"
            }
          ]
      },
      { "category" : "Replication",
        "organisms" : [ { "experiments" : [ { "experiment_title" : "Replication Timing Characterization",
                    "labs" : [ "David MacAlpine" ],
                    "pi" : "David MacAlpine"
                  },
                  { "experiment_title" : "MacAlpine Early Origin of Replication Identification",
                    "labs" : [ "David MacAlpine" ],
                    "pi" : "David MacAlpine"
                  },
                  { "experiment_title" : "Genome-wide localization of essential replication initiators",
                    "labs" : [ "David MacAlpine",
                        "Terry Orr-Weaver"
                      ],
                    "pi" : "David MacAlpine"
                  },
                  { "experiment_title" : "Genome-wide localization of essential replication initiators by ChIP-chip",
                    "labs" : [ "David MacAlpine",
                        "Terry Orr-Weaver"
                      ],
                    "pi" : "David MacAlpine"
                  }
                ],
              "organism" : "D. melanogaster"
            },
            { "experiments" : [  ],
              "organism" : "C. elegans"
            }
          ]
      },
      { "category" : "TF binding sites",
        "organisms" : [ { "experiments" : [ { "experiment_title" : "Chromatin Binding Site Mapping",
                    "labs" : [ "Kevin White" ],
                    "pi" : "Kevin White"
                  },
                  { "experiment_title" : "Chromatin Binding Site Mapping of Transcription Factors in D. melanogaster by ChIP-seq",
                    "labs" : [ "Kevin White" ],
                    "pi" : "Kevin White"
                  }
                ],
              "organism" : "D. melanogaster"
            },
            { "experiments" : [ { "experiment_title" : "ChIP-Seq Identification of C. elegans TF Binding Sites",
                    "labs" : [ "Gerstein",
                        "Michael Snyder"
                      ],
                    "pi" : "Michael Snyder"
                  } ],
              "organism" : "C. elegans"
            }
          ]
      }
    ]
}