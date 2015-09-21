#!/usr/bin/env bash

DIST_DIR='../../dist/style/'
DIST_FILE='portfolio.css'
DIST_PATH="${DIST_DIR}${DIST_FILE}"

SRC_FILES="style.css sizes.css colors.css"

echo "/* ${DIST_FILE} generated from ${SRC_FILES} */" > ${DIST_PATH}

cat ${SRC_FILES} >> ${DIST_PATH}
