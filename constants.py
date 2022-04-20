from menu import find_all_claims, find_all_manifestations, find_all_praise, find_all_seggestions, find_one_manifestation, create_manifestation, exit_system

from enum import Enum


class MenuStatus(Enum):
    FIND_ALL_MANIFESTATIONS = 1
    FIND_ALL_SUGGESTIONS = 2
    FIND_ALL_CLAIMS = 3
    FIND_ALL_PRAISE = 4
    CREATE_MANIFESTATION = 5
    FIND_ONE_MANIFESTATION = 6
    EXIT = 7

accept_key_menu = {
    MenuStatus.FIND_ALL_MANIFESTATIONS.value: find_all_manifestations,
    MenuStatus.FIND_ALL_SUGGESTIONS.value: find_all_seggestions,
    MenuStatus.FIND_ALL_CLAIMS.value: find_all_claims,
    MenuStatus.FIND_ALL_PRAISE.value: find_all_praise,
    MenuStatus.CREATE_MANIFESTATION.value: create_manifestation,
    MenuStatus.FIND_ONE_MANIFESTATION.value: find_one_manifestation,
    MenuStatus.EXIT.value: exit_system
}
