# -*- coding: utf-8 -*-
from typing import Union

import pandas as pd

from zvt.selectors.zvt_selector import TechnicalSelector
from zvt.trader.trader import Trader
from zvt.utils.utils import marshal_object_for_ui


class SingleCoinTrader(Trader):
    entity_type = SecurityType.coin

    def __init__(self,
                 security: str = 'coin_binance_EOS/USDT',
                 start_timestamp: Union[str, pd.Timestamp] = '2018-06-01',
                 end_timestamp: Union[str, pd.Timestamp] = '2019-06-30',
                 provider: str = 'ccxt',
                 level: Union[str, IntervalLevel] = IntervalLevel.LEVEL_1DAY,
                 trader_name: str = None,

                 kdata_use_begin_time: bool = True) -> None:
        super().__init__([security], SecurityType.coin, None, None, start_timestamp, end_timestamp, provider,
                         level, trader_name, real_time, kdata_use_begin_time=kdata_use_begin_time)

    def init_selectors(self, entity_ids, entity_type, exchanges, codes, start_timestamp, end_timestamp):
        self.selectors = []

        selector1 = TechnicalSelector(entity_ids=entity_ids, entity_type=entity_type,
                                      exchanges=exchanges, codes=codes,
                                      start_timestamp=start_timestamp,
                                      end_timestamp=end_timestamp, level=IntervalLevel.LEVEL_1DAY,
                                      provider='ccxt')
        selector1.run()

        # selector2 = TechnicalSelector(entity_ids=entity_ids, entity_type=entity_type,
        #                                    exchanges=exchanges, codes=codes,
        #                                    start_timestamp=start_timestamp,
        #                                    end_timestamp=end_timestamp, level=IntervalLevel.LEVEL_5MIN,
        #                                    provider='ccxt')
        # selector2.run()

        self.selectors.append(selector1)
        # self.selectors.append(selector2)

    @classmethod
    def get_constructor_meta(cls):
        meta = super().get_constructor_meta()
        meta.metas['entity_type'] = marshal_object_for_ui(cls.entity_type)
        return meta


if __name__ == '__main__':
    SingleCoinTrader().run()
