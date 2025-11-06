#!/bin/bash
# ===============================================
# setup_acts_env.sh
# 用于自动加载 LCG105 + oddenv + ACTS 环境
# Author: Renjie Yu
# ===============================================

# 颜色格式
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color
source oddenv/bin/activate
echo -e "${YELLOW}>>> Loading LCG_105 environment...${NC}"
source /cvmfs/sft.cern.ch/lcg/views/LCG_105/x86_64-el9-gcc13-opt/setup.sh

echo -e "${YELLOW}>>> Activating virtual environment (oddenv)...${NC}"
source /afs/cern.ch/user/r/reyu/public/acts-odd-4d-vertexing-performance/oddenv/bin/activate

# 安装必要的 Python 包（仅首次执行时有效）
if ! python -c "import snakemake" &> /dev/null; then
    echo -e "${YELLOW}Installing Snakemake...${NC}"
    pip install snakemake
fi

if ! python -c "import pulp" &> /dev/null; then
    echo -e "${YELLOW}Installing pulp==2.7.0...${NC}"
    pip install pulp==2.7.0
fi

echo -e "${YELLOW}>>> Setting PYTHONPATH for scripts and acts-install...${NC}"
export PYTHONPATH=/afs/cern.ch/user/r/reyu/public/acts-odd-4d-vertexing-performance/scripts:"$PYTHONPATH"
export PYTHONPATH=/afs/cern.ch/user/r/reyu/public/acts-install/python:"$PYTHONPATH"

echo -e "${YELLOW}>>> Loading ACTS environment...${NC}"
source /afs/cern.ch/user/r/reyu/public/acts-install/bin/this_acts.sh
source /afs/cern.ch/user/r/reyu/public/acts-install/python/setup.sh

echo -e "${GREEN}>>> Environment setup completed successfully!${NC}"

export ODD_PATH=/afs/cern.ch/user/r/reyu/private/acts-main/thirdparty/OpenDataDetector
export LD_LIBRARY_PATH=$ODD_PATH/factory:$LD_LIBRARY_PATH

source /afs/cern.ch/user/r/reyu/public/odd-install/this_odd.sh

echo ">>>ok"
